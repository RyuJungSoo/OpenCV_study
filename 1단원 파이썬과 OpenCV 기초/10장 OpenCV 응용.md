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
# 10.2 마우스 이벤트 활용하기
마우스 이벤트 활용을 위해 OpenCV에서는 **setMouseCallback 함수**를 제공하고 있다. 마우스 버튼 클릭, 드래그 등 마우스 입력 장치 관련 이벤트가 발생할 경우 처리할 함수를 
CallBack 함수로 정의를 해두고, 이 함수를 지정하면 손쉽게 마우스 이벤트 활용이 가능하다.
```py
import cv2
import numpy as np

def draw_rectangle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # 왼쪽 마우스를 더블 클릭하면
        cv2.rectangle(img, (x,y), (x+50,y+50), (255,0,0), -1) # 해당 img의 위치에 사각형 그리기 ((B, G, R) 순), (두께 값이 -1이므로 도형 색 채우기) 

# callback 함수
img = np.zeros((512, 512, 3), np.uint8) # 가로 세로 512 픽셀이면서 3채널 모두 값이 0인 img 행렬 만들기 (np.uint8 -> 부호가 없는 정수)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle) 

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
```
[cv2.rectangle에 대해서](https://copycoding.tistory.com/146)         

# 10.3 카메라 영상에 시간 출력
OpenCV에서는 외부 카메라 입력을 손쉽게 구현할 수 있다. OpenCV에서는 **VideoCapture 클래스**를 사용하여 WebCam 및 IP Camera를 연결할 수 있다.

```py
import cv2
import time

CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID) # 웹캠 켜기
if cam.isOpened() == False: # cam이 열리지 않는 경우
    print('Can not open the Camera(%d)' %(CAMERA_ID))
    exit()

cv2.namedWindow('CAM_Window')

while(True):
    ret, frame = cam.read()

    now = time.localtime() # 현재 지역의 시간대를 now에 저장
    str = "%d. %d. %d. %d:%d:%d" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec) # 시간을 문자열로 변경

    # 현재 frame에 str을 위치 (0, 100)에 cv2.FONT_HERSHEY_SCRIPT_SIMPLEX 폰트, 크기 1, 색상 (255,255,0)으로 띄우기 
    cv2.putText(frame, str, (0,100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255,255,0))

    cv2.imshow('CAM_Window', frame)

    
    if cv2.waitKey(10) >= 0:
        break

cam.release()
cv2.destroyWindow('CAM_Window')
```
[cv2.putText에 대해서](https://copycoding.tistory.com/151)                     

# 10.4 TrackBar 예제
윈도우 프로그래밍을 하다 보면 **트랙바 클래스**를 활용할 경우가 있다. 특히 포토샵과 같이 제한된 범위의 값을 조절하면서 
이미지의 변화 상태를 직관적으로 확인이 필요할 경우 주로 사용된다. OpenCV에서는 이와 같은 트랙바를 매우 편하게 활용할 수 있도록 제공한다.     
(cv2.createTrackbar -> 트랙바 값의 변화가 있을 때마다 콜백 함수를 지정하여 처리가 가능)          
[cv2.createTrackbar, cv2.getTrackbarPos에 대해서](https://seokii.tistory.com/5)                

```py
import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow('RGB track bar') # 윈도우 생성

# 트랙바를 생성하면서 생성될 윈도우를 지정한다. (콜백 함수는 따로 지정하지 않았음) 
cv2.createTrackbar('Red color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('Green color', 'RGB track bar', 0, 255, nothing)
cv2.createTrackbar('Blue color', 'RGB track bar', 0, 255, nothing)

# 트랙바 생성 시 초깃값
cv2.setTrackbarPos('Red color', 'RGB track bar', 125)
cv2.setTrackbarPos('Green color', 'RGB track bar', 125)
cv2.setTrackbarPos('Blue color', 'RGB track bar', 125)

img = np.zeros((512, 512, 3), np.uint8)

while(1):
    # 트랙바의 현재값 읽어오기
    redval = cv2.getTrackbarPos('Red color', 'RGB track bar')
    greenval = cv2.getTrackbarPos('Green color', 'RGB track bar')
    blueval = cv2.getTrackbarPos('Blue color', 'RGB track bar')

    cv2.rectangle(img, (0,0), (512, 512), (blueval, greenval, redval), -1)
    cv2.imshow('RGB track bar', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindow()
```
