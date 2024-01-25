import numpy as np
import cv2

# 마우스 클릭 함수
def onMouse(event, x, y, flags, param):
    global radius, line_width
    if event == cv2.EVENT_LBUTTONDOWN:
        # 왼쪽 버튼 누르면 정사각형 그리기
        cv2.rectangle(image, (x, y), (x + 30, y + 30), (0, 0, 255), line_width) # 30 by 30 정사각형
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        # 오른쪽 버튼 누르면 원 그리기
        cv2.circle(image, (x, y), radius, (0, 0, 255), line_width) # 마우스클릭 event좌표 중심으로 원그리기
        cv2.imshow(title, image)

# 트랙바 원 반지름 반환함수
def onChangeRadius(value):
    global radius
    radius = value
# 트랙바 선굵기 반환 함수
def onChangeLineWidth(value):
    global line_width
    line_width = value

image = np.zeros((300,500,3),np.uint8)
image[:] = 255
title = 'chanyoung' #상태바 제목
cv2.imshow(title, image)

radius = 20
line_width = 1
# 트랙바 생성
cv2.createTrackbar('Radius', title, radius, 50, onChangeRadius)
cv2.createTrackbar('Line Width', title, line_width, 10, onChangeLineWidth)

cv2.setMouseCallback(title, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()