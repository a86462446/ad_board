from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from .models import Video
import os
import subprocess
import json
import cv2

# Home page
def index(request):
    return render(request, 'index.html')

# Upload file page
def upload_file(request):
    # 請求是POST時，表示用戶提交了表單
    if request.method == 'POST':
        # 取得表單中的檔案
        form = UploadFileForm(request.POST, request.FILES)

        # 檢查表單是否有效
        if form.is_valid():
            # 取得檔案列表
            files = request.FILES.getlist('file')

            # 檢查是否有選擇檔案
            if len(files) < 1:
                # 沒有選擇檔案，則返回錯誤訊息
                return render(request, 'upload_file.html', {'message':'請至少選擇一個檔案！'})
            # 取得目標目錄的路徑
            fs = FileSystemStorage()
            # 將檔案存入目標目錄
            for file in files:
                database= Video(videoname= file.name)
                database.save()

                fs.save(file.name, file)
            # 返回成功訊息
            return render(request, 'upload_file.html', {'message':'Upload Successfully.'})
    # 請求是GET時，表示用戶訪問了上傳頁面
    else:
        # 返回上傳頁面
        form = UploadFileForm()
    # 返回上傳頁面
    return render(request, 'upload_file.html', {'form': form})

# Play page
def play(request):
    # 取得目標目錄的路徑
    directory = os.path.join(settings.MEDIA_ROOT)
    # 讀取目錄中的所有文件
    files = os.listdir(directory)
    # 傳遞文件列表到模板中
    files_path = [os.path.join(settings.MEDIA_URL,file) for file in files]
    # 存取每個檔案的路徑
    context = {
        'media_files':files_path
    }
    # 返回包含檔案路徑的播放頁面
    return render(request, 'play.html', context)

# 選擇要撥放的檔案，並且開啟檔案
def show_file(request, file_path):
    
    try:
        # 取得檔案的完整路徑
        file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
        # 開啟檔案
        subprocess.run(['open', file_full_path]) # MacOS

        """選擇伺服器的作業系統
        subprocess.run(['xdg-open', file_full_path]) # Linux/Mac
        subprocess.run(['open', file_full_path]) # MacOS
        subprocess.run(['start', '', file_full_path], shell=True) # Windows
        """

        # 使用 AppleScript 控制應用程式全螢幕顯示
        applescript = '''
        tell application "System Events"
            tell process "QuickTime Player" -- 將 "應用程式名稱" 改為實際的應用程式名稱
                keystroke "f" using {control down, command down} -- 模擬按下 Control + Command + F 全螢幕顯示
            end tell
        end tell
        '''
        subprocess.call(["osascript", "-e", applescript])
        
        # 開啟檔案成功，返回上一頁，不然路徑會變成檔名
        return HttpResponse('<script>window.history.back();</script>')

    except:
        # 開啟檔案失敗，返回錯誤訊息
        return render(request, 'play.html', {'message':'File not found！'})

# 刪除檔案
def delete(request):
    # 取得要刪除的檔案路徑
    file_path = request.POST.get('file')
    # 呼叫delete_file函式，並且把回傳值傳給response
    response = delete_file(file_path)
    # 返回刪除頁面，並且把response和file_path傳給刪除頁面
    return render(request, 'delete.html', {'message':response,'file':file_path})

# Delete file
def delete_file(file_path):
    # 把路徑中的/media/去掉，因為MEDIA_ROOT中已經有/media/了
    file_path = file_path[7:]
    # 取得檔案的完整路徑
    file_full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    # 刪除檔案
    os.remove(file_full_path)
    # 返回刪除成功訊息
    return 'Successfully deleted.'

# 控制撥放器 (暫停、關閉)
def control_player(request):
    # 取得請求的方法
    if request.method == 'POST':
        # 取得請求的資料
        data = json.loads(request.body)
        
        # 取得請求的動作
        action = data.get('action')
        
        # 請求是Stop時，表示用戶按下了關閉按鈕
        if action == 'Stop':
            subprocess.call(['osascript', '-e', 'quit app "VLC"'])

    return JsonResponse({'message':'success'}) # 返回成功訊息
