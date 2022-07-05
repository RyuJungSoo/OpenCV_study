import os

# 폴더 생성하기
def createFolder(dir):
    try:
        if not os.path.exists(dir): # 해당 경로 또는 폴더가 존재하지 않으면
            os.makedirs(dir) # 폴더 또는 경로 생성
    except OSError:
        print ('Error: createFolder')
