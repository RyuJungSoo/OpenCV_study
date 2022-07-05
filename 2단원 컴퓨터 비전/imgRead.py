import cv2

# 영상을 불러오기
def imgRead(imgPath, imgReadType, imgResWidth, imgResHeight):
    img = cv2.imread(imgPath, imgReadType) # imgPath의 파일을 imgReadType으로 불러오기
    if imgResHeight != 0 | imgResWidth != 0:
        img = cv2.resize(img, (imgResWidth, imgResHeight)) # 이미지 크기 조정
    return img
