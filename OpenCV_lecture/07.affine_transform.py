import numpy as np, cv2

image = cv2.imread('./images/myart_test.png', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")

center = (200, 200) # 회전 변환 기준 좌표
angle, scale = 30, 1 # 회전 각도, 크기 지정 - 크기 변경은 안 함
size = image.shape[::-1] # 영상크기는 행렬 행태의 역순
pt1 = np.array([( 30, 70),(20, 240), (300, 110)], np.float32) # 변환 전 3개 좌표 지정
pt2 = np.array([(120, 20),(10, 180), (280, 260)], np.float32) # 변환 후 3개 좌표 지정
aff_mat = cv2.getAffineTransform(pt1, pt2) # 3개 좌표 쌍으로 어파인 행렬 생성
rot_mat = cv2.getRotationMatrix2D(center, angle, scale) # 회전 변환을 위한 어파인 행렬
dst3 = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)
dst4 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)


image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR )

for i in range(len(pt1)):
    cv2.circle(image, tuple(pt1[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst3 , tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.imshow("dst3_OpenCV_affine", dst3); cv2.imshow("dst4_OpenCV_affine_rotate", dst4)
cv2.waitKey(0)