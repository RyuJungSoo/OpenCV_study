# 10.1 동영상 파일 활용하기
OpenCV 라이브러리에서는 다양한 포맷의 입력 데이터를 활용할 수 있다. 그중에서도 가장 많이 활용되는 입력 포맷으로 동영상 파일과 USB 카메라가 대표적이다.    
```py
import cv2

#cap 변수에 비디오 파일 포인터를 지정하기
#cap = cv2.VideoCapture("vtest.avi")
cap = cv2.VideoCapture(0) # Default camera(웹캠 켜기)

while cap.isOpened(): # cap이 열려있는 동안
    # 한 장의 이미지(frame)를 가져오기
    # 영상 : 이미지(프레임)의 연속
    # 정상적으로 읽어왔는지 -> retval
    # 읽어온 프레임 -> frame
    
    success, frame = cap.read() 
    if success:
        cv2.imshow('image', frame) # image라는 창에 frame 보여주기

        # 1초 지난 후에 다음 프레임을 보여줌
        key = cv2.waitKey(1) & 0xFF # (0xFF를 & 연산한 이유는 운영체제가 64비트여서)
        if(key == 27): # 입력된 키 값이 esc(아스키 코드 27)이면
            break
    else: # 프레임정보를 정상적으로 읽지 못하면
        break

cap.release() # 영상 파일(카메라) 사용 종료
cv2.destroyAllWindows() # 생성한 모든 윈도 제거
```

