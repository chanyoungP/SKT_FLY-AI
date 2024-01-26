# 연습문제 2
# median2.jpg를 이용하여 소금-후추 노이즈를 만들고, 
# 침식과 팽창 연산을 적용해 보라
import numpy as np, cv2

# 노이즈 제작 함수
def salt_pepper_noise(img, n):
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for (x,y) in zip(x,y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255

    return noise

# erode
def erode(image):
    data = [0, 1, 0,                                               # 마스크 선언 및 초기화
        1, 1, 1,
        0, 1, 0]
    mask = np.array(data, np.uint8).reshape(3, 3)
    th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]  # 영상 이진화
    dst2 = cv2.morphologyEx(th_img, cv2.MORPH_ERODE, mask)         # OpenCV의 침식 함수
    return dst2

# dilate
def dilate(image):
    mask = np.array([[0, 1, 0],                         # 마스크 초기화
                 [1, 1, 1],
                 [0, 1, 0]]).astype("uint8")
    th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]  # 영상 이진화                    
    dst2 = cv2.morphologyEx(th_img, cv2.MORPH_DILATE, mask)  # OpenCV의 팽창 함수
    return dst2

# 이미지 읽어오기
image = cv2.imread("./images/median2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
# 노이즈 만들기   
noise = salt_pepper_noise(image, 500)
#med_img2 = cv2.medianBlur(noise, 3) # OpenCV 제공 함수
cv2.imwrite('./noise.jpg', noise)
# erode 침식
erode_img = erode(noise)
# dilate 팽창
dilate_img = dilate(erode_img)

cv2.imshow("image", image),
cv2.imshow("noise", noise),
cv2.imshow("erode", erode_img),
cv2.imshow("dilate",dilate_img),
cv2.waitKey(0)