import cv2
import numpy as np 

image = cv2.imread("./images/bright.jpg", cv2.IMREAD_GRAYSCALE)    # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")

# OpenCV 함수 이용
dst1 = cv2.add(image,100)
dst2 = cv2.subtract(image,100)


#numay로 
dst3 = image + 100
dst4 = image - 100 


#exp
def image_exp(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat.item(i,j)
            mat.itemset((i,j),np.exp(k))
dst5 = image.copy()
image_exp(dst5)

cv2.imshow("original image", image)
cv2.imshow("dst1- bright: OpenCV", dst1)
cv2.imshow("dst2- dark: OpenCV", dst2)
cv2.imshow("dst3- bright: numpy", dst3)
cv2.imshow("dst4- dark: numpy", dst4)
cv2.imshow("dst4- dark: exp", dst5);
cv2.waitKey(0)