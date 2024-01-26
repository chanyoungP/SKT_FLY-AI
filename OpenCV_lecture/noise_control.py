# import cv2
# import numpy as np

# def on_trackbar_noise(value):
#     global noise_level
#     noise_level = value
#     update_image_with_noise()

# def update_image_with_noise():
#     # 노이즈 생성
#     noise = np.zeros_like(image)
#     cv2.randn(noise, 0, noise_level)

#     # 노이즈를 이미지에 추가
#     noisy_image = cv2.add(image, noise)

#     # 이미지 표시
#     cv2.imshow('Noisy Image', noisy_image)

# # 이미지 읽기
# image = cv2.imread('./images/myart_test.png', cv2.IMREAD_GRAYSCALE)
# if image is None:
#     raise Exception("영상 파일 읽기 오류 발생")

# # 초기 노이즈 레벨 설정
# max_noise = 1000

# noise_level = max_noise

# # 윈도우 생성
# cv2.namedWindow('Noisy Image')

# # 트랙바 생성
# cv2.createTrackbar('Noise Level', 'Noisy Image', noise_level, max_noise, on_trackbar_noise)

# # 초기 노이즈 추가된 이미지 표시
# update_image_with_noise()

# # 키 이벤트 대기
# cv2.waitKey(0)
# cv2.destroyAllWindows()


## gradually image show 
import cv2
import numpy as np

def on_trackbar(value):
    global alpha
    alpha = value / 100.0
    update_image()

def update_image():
    result = (alpha/100) * art_image
    cv2.imshow('MyArt Test', result)

# 흰색 배경 이미지 생성
background = 255 * np.ones((500, 500, 3), dtype=np.uint8)

# 그림 이미지 읽기
art_image = cv2.imread('./images/myart_test.png')

if art_image is None:
    raise Exception("이미지 파일 읽기 오류 발생")

# 이미지 크기 조정
art_image = cv2.resize(art_image, (500, 500))

# 초기 알파 값 설정
alpha = 0

# 윈도우 생성
cv2.namedWindow('MyArt Test')

# 트랙바 생성
cv2.createTrackbar('Alpha', 'MyArt Test', int(alpha), 100, on_trackbar)

# 초기 이미지 표시
update_image()

# 키 이벤트 대기
cv2.waitKey(0)
cv2.destroyAllWindows()
