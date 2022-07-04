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

        # 1ms 지난 후에 다음 프레임을 보여줌
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

# 10.5 아날로그 시계 예제
아날로그 시계 예제는 시스템의 현재 시각을 가져오는 시스템 함수의 용법과 선, 원을 그리는 그래픽 함수 그리고 좌표 변환에 대한 복합적인 학습이 가능하기 때문이다.         
예제를 작성하기 전에 시계의 시침이 가리키는 위치가 (x, y)이고 시침의 길이가 1이라 하면 아래그림과 같이 **삼각함수**를 사용하여 그릴 수 있다. 예제에서는 시침의 이동량을 
육십분법으로 계산하고 삼각함수에 입력할 때 호도법으로 변환하였다.                                    
(삼각함수를 사용하기 위해서는 **math 모듈**을 임포트 해야 한다.)                     
<img src="https://user-images.githubusercontent.com/81175672/177108997-1696c9fc-b211-4226-903e-bf3846e430da.JPG"  width="500" height="500"/>
```py
import cv2
import time
from math import *
import numpy as np

cv2.namedWindow('Clock')

# img 행렬 만들기
img = np.zeros((512,512,3), np.uint8)

while(True):
    # img에 중심이 (256, 256), 반지름이 250, 색깔이 (125, 125, 125)이고 속이 꽉 찬 원을 그리기
    cv2.circle(img, (256,256), 250, (125,125,125), -1)

    now = time.localtime()
    hour = now.tm_hour
    min = now.tm_min

    # 12시인 경우 0시로 초기화
    if hour > 12:
        hour -= 12

    # 시침과 분침이 0시부터 이루는 각을 계산
    Ang_Min = min * 6 # 분침은 한 칸당 6도 (360/60)
    Ang_Hour = hour*30+min*0.5 # 시침은 한 칸당 30도(360/12), 분침이 이동하는 동안 시침도 이동하므로 추가로 0.5도 이동해야 함(360/(12*60))


    # 시침 표시(호도법 사용)
    if(hour == 12 or 1 <= hour <= 2):
        x_pos = int(150.0*cos((90.0-Ang_Hour)*3.141592/180))
        y_pos = int(150.0*sin((90.0-Ang_Hour)*3.141592/180))
        cv2.line(img, (256, 256), (256 + x_pos, 256 - y_pos), (0, 255, 0), 6)

    elif(3 <= hour <= 5):
        x_pos = int(150.0*cos((Ang_Hour-90.0)*3.141592/180))
        y_pos = int(150.0*sin((Ang_Hour-90.0)*3.141592/180))
        cv2.line(img, (256, 256), (256 + x_pos, 256 + y_pos), (0, 255, 0), 6)

    elif(6 <= hour <= 8):
        x_pos = int(150.0*sin((Ang_Hour-180.0)*3.141592/180))
        y_pos = int(150.0*cos((Ang_Hour-180.0)*3.141592/180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 + y_pos), (0, 255, 0), 6)
        
    elif(9 <= hour <= 11):
        x_pos = int(150.0*cos((Ang_Hour-270.0)*3.141592/180))
        y_pos = int(150.0*sin((Ang_Hour-270.0)*3.141592/180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 - y_pos), (0, 255, 0), 6)


    # 분침 표시(호도법 사용)
    if(min == 00 or 1 <= min <= 14):
        x_pos = int(200.0*cos((90.0-Ang_Min)*3.141592/180))
        y_pos = int(200.0*sin((90.0-Ang_Min)*3.141592/180))
        cv2.line(img, (256, 256), (256 + x_pos, 256 - y_pos), (255, 0, 0), 1)

    elif(15 <= min <= 29):
        x_pos = int(200.0*cos((Ang_Min-90.0)*3.141592/180))
        y_pos = int(200.0*sin((Ang_Min-90.0)*3.141592/180))
        cv2.line(img, (256, 256), (256 + x_pos, 256 + y_pos), (255, 0, 0), 1)

    elif(30 <= min <= 44):
        x_pos = int(200.0*sin((Ang_Min-180.0)*3.141592/180))
        y_pos = int(200.0*cos((Ang_Min-180.0)*3.141592/180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 + y_pos), (255, 0, 0), 1)
        
    elif(45 <= min <= 59):
        x_pos = int(200.0*cos((Ang_Min-270.0)*3.141592/180))
        y_pos = int(200.0*sin((Ang_Min-270.0)*3.141592/180))
        cv2.line(img, (256, 256), (256 - x_pos, 256 - y_pos), (255, 0, 0), 1)

    cv2.imshow('Clock', img)
    if cv2.waitKey(10) >= 0:
        break


cv2.destroyWindow('Clock')
```

# 10.6 자유 낙하 운동
**자유 낙하 운동**은 공기 저항과 모든 마찰을 무시하고 공중에 정지한 물체를 떨어뜨려 물체가 중력에 의해서만 낙하하는 등가속도 운동을 말한다.    
중력에 의해서만 낙하하므로 가속도는 중력가속도와 같으며 초기 속도는 0이다.
```py
import cv2
from math import*
import numpy as np

cv2.namedWindow("Free Fall")

width = 512
height = 960
img = np.zeros((height, width, 3), np.uint8)

time = ypos = 0
while(True):
    if(ypos+30) < height:
        cv2.circle(img, (256, 30+ypos), 10, (255,0,0), -1)
        time += 1
        ypos = int((9.8*time**2)/2)
        print(time, ':', ypos)
    cv2.imshow('Free Fall', img)
    if cv2.waitKey(100) >= 0:
        break

cv2.destroyWindow('Free Fall')

```
[cv2.circle에 대해서](https://copycoding.tistory.com/147)
# 10.7 포물선 운동
이번 실습 예제는 비스듬히 던진 물체의 포물선 운동에 대한 프로그램을 만들어 보자.         
물체를 던지는 각도를 θ라 할 때 x축 속도는 v<sub>x</sub> 이고, y축 이동속도는 v<sub>y</sub> 이다.              
v<sub>0</sub>는 초기 이동속도, g는 중력 가속도, t는 시간이 된다.       
```py
import cv2
from math import *
import numpy as np

init_Vel = float(input("초기 속도를 입력하세요 : "))
init_Ang = float(input("초기 각도를 입력하세요 : "))
cv2.namedWindow('Parabolic Motion')

width = 960
height = 960
img = np.zeros((height, width,3), np.uint8)

time = xpos = ypos = 0
init_posx = 30
init_posy = 250
Vel_x = int(init_Vel*cos(init_Ang*pi/180.0))
Vel_y = int(-1.0*init_Vel*sin(init_Ang*pi/180.0))

while(True):
    if (ypos+30) < height:

        cv2.circle(img, (init_posx+xpos, init_posy+ypos), 10, (255,0,0), -1)
        time+=0.2
        Vel_y = int(Vel_y + 9.8*time)

        xpos = int(xpos+Vel_x*time)
        ypos = ypos + int(Vel_y*time) + int((9.8 * time **2)/2)
        print(time, ':', xpos, ypos)

    cv2.imshow('Parabolic Motion', img)

    if cv2.waitKey(100) >= 0:
        break

cv2.destroyWindow('Parabolic Motion')

```
# 10.8 피보나치 수열 그래픽
이번 실습에서는 피보나치 수열을 이용하여 황금비율을 가지는 그래픽을 그려보도록 하자.            
곡선을 그리기 위해 OpenCV의 **ellipse 함수**를 사용한다.
```py
import cv2
from math import *
import numpy as np

cv2.namedWindow('Pibonacci graphic')

width = 960
height = 960
img = np.zeros((height,width,3), np.uint8)

init_posx = 480
init_posy = 480
drawing_unit = 5
idx, a, b = 0,0,1

while a < 70:
    cv2.imshow('Pibonacci graphic', img)
    a,b = b, a+b
    Begin_Ang = int(90*(idx%4))
    End_Ang = int(90*(idx%4+1))
    if Begin_Ang == 0:
        init_posx -= (b-a) * drawing_unit
    elif Begin_Ang == 90:
        init_posy -= (b-a) * drawing_unit
    elif Begin_Ang == 180:
        init_posx += (b-a) * drawing_unit
    elif Begin_Ang == 270:
        init_posy += (b-a) * drawing_unit

    print(idx, 'turn : ', 'Pibonacci number -', b)
    cv2.ellipse(img, (init_posx, init_posy), (b*drawing_unit, b*drawing_unit),0, Begin_Ang,End_Ang, (0,255,0),2)

    idx+=1

while(True):
    if cv2.waitKey(10) >= 0:
        break
cv2.destroyWindow('Pibonacci graphic')

```
