# import cv2
# import numpy as np

# def on_trackbar_low(value):
#     global low_threshold
#     low_threshold = value
#     update_edges()

# def on_trackbar_high(value):
#     global high_threshold
#     high_threshold = value
#     update_edges()

# def update_edges():
#     edges = cv2.Canny(image, low_threshold, high_threshold)
#     cv2.imshow('Canny Edges', edges)

# # 이미지 읽기
# image = cv2.imread('./images/cannay_tset.jpg', cv2.IMREAD_GRAYSCALE)
# if image is None: raise Exception("영상 파일 읽기 오류 발생")

# # 초기 임계값 설정
# low_threshold = 50
# high_threshold = 100

# # 윈도우 생성
# cv2.namedWindow('Canny Edges')

# # 트랙바 생성
# cv2.createTrackbar('th1', 'Canny Edges', low_threshold, 255, on_trackbar_low)
# cv2.createTrackbar('th2', 'Canny Edges', high_threshold, 255, on_trackbar_high)

# # 초기 에지 표시
# update_edges()

# # 키 이벤트 대기
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#### edge 색 반전
import cv2
import numpy as np

def on_trackbar_low(value):
    global low_threshold
    low_threshold = value
    update_edges()

def on_trackbar_high(value):
    global high_threshold
    high_threshold = value
    update_edges()

def update_edges():
    edges = cv2.Canny(image, low_threshold, high_threshold)
    edges_inverted = cv2.bitwise_not(edges)  # 에지를 흰색으로, 배경을 검은색으로 반전
    cv2.imshow('Canny Edges', edges_inverted)

# 이미지 읽기
image = cv2.imread('./images/myart_test.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 초기 임계값 설정
low_threshold = 50
high_threshold = 100

# 윈도우 생성
cv2.namedWindow('Canny Edges')

# 트랙바 생성
cv2.createTrackbar('th1', 'Canny Edges', low_threshold, 255, on_trackbar_low)
cv2.createTrackbar('th2', 'Canny Edges', high_threshold, 255, on_trackbar_high)

# 초기 에지 표시
update_edges()

# 키 이벤트 대기
cv2.waitKey(0)
cv2.destroyAllWindows()

