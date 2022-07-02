# 9.1 OpenCV 개요
**OpenCV**는 라이브러리 중 하나로서 영상 처리 또는 영상 인식 관련 소스들을 모아 놓은 라이브러리이다.       
OpenCV는 약 2500개가 넘는 영상 처리 알고리즘이 최적화되어서 포함되어 있으며 이 알고리즘들을 활용하는 것에만 집중할 수 있도록 만들어져 있다. 
상황에 따라서는 알고리즘을 직접 구현하는 것이 더 좋을 수도 있지만, 일반적인 경우 알고리즘에 대한 기초적인 이해만 가지고 OpenCV를 사용하는 것이 생산성이 높다.      


# 9.2 OpenCV 설치
명령 프롬프트를 실행하고 파이썬이 설치된 디렉터리에서 pip을 업그레이드해 준다.
~~~
python -m pip install --upgrade pip
~~~
다음으로 opencv-python와 opencv-contrib-python을 설치한다.
~~~
python -m pip install opencv-python
~~~

~~~
python -m pip install opencv-contrib-python
~~~

# 9.3 OpenCV 응용 프로젝트 만들기
```py
import cv2
img = cv2.imread("image.jpg", 1)
cv2.namedWindow("image") # image라는 이름을 갖는 창 생성
cv2.imshow("image", img) # image 창에 이미지 표시
cv2.waitKey() # 아무키나 누르면
```
**<실행 결과>**                  
<img src="https://user-images.githubusercontent.com/81175672/177002367-939fb122-aac8-40e2-ad47-bfab2b956878.JPG"  width="450" height="450"/>


# 9.4 OpenCV 기본 자료형
OpenCV 라이브러리는 사용 목적 자체가 영상을 다루는 만큼 "영상" 또는 "이미지"에 대한 자료형이 필요하다.     
객체(class) 기반의 **Mat** 자료형을 사용하며 Mat의 멤버 변수로 uchr* 타입의 data 포인터 변수가 있는데 이 변수는 Matrix의 Data를 
가리키는 포인터 변수이다.           
영상 데이터는 3가지 색상(붉은색, 초록색, 파란색) 채널로 구성되어 있으며, RGB 채널의 픽셀별 데이터는 다음 그림과 같이 붉은색, 초록색, 파란색이 반복되면서 저장된다.
![KakaoTalk_20220702_215159075](https://user-images.githubusercontent.com/81175672/177001569-240ed9d6-6130-4086-b999-7483dfe57742.jpg)         

OpenCV의 Mat 자료형 외에도 numpy array를 통해서 영상의 픽셀별 제어가 가능하다.                                
**imread 함수**를 통해 반환되는 img는 numpy의 array 타입이며 array의 원소, 즉 픽셀을 제어하기 위해서는 **itemset**을 사용할 수 있다.

~~~
<itemset>
img.itemset(y좌표(or 행), x좌표(or 열), 채널, 채널 값)
~~~

```py
import numpy as np
import cv2 as cv

img = cv.imread('image.jpg')

height = img.shape[0] # 이미지의 높이(행렬의 행 갯수)
width = img.shape[1] # 이미지의 너비(행렬의 열 갯수)

for y in range(0, height):
    img.itemset(y, int(width/2), 0, 0) # 붉은색 채널 값 0
    img.itemset(y, int(width/2), 1, 0) # 초록색 채널 값 0
    img.itemset(y, int(width/2), 2, 255) # 파란색 채널 값 255
    
for x in range(0, width):
    img.itemset(int(height/2), x, 0, 255) # 붉은색 채널 값 255
    img.itemset(int(height/2), x, 1, 0) # 초록색 채널 값 0
    img.itemset(int(height/2), x, 2, 0) # 파란색 채널 값 0

cv.imshow('win', img) # win 창에 이미지 표시
cv.waitKey(0)

```
[numpy.shape()에 대해서](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sw4r&logNo=221581585204)
[imshow에 대해서](https://webnautes.tistory.com/796)

**<실행 결과>**        
<img src="[https://user-images.githubusercontent.com/81175672/177002367-939fb122-aac8-40e2-ad47-bfab2b956878.JPG](https://user-images.githubusercontent.com/81175672/177002389-1266b9d9-3221-419a-81d7-cf76958e680f.JPG)"  width="450" height="450"/>

