# import numpy as np, cv2

# image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
# image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
# if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")


# # 영상 합성
# alpha,beta = 0.6,0.7
# # cv2.namedWindow("result")
# # alpha = cv2.getTrackbarPos("alpha", "result")
# # beta = cv2.getTrackbarPos("beta", "result")
# add_img1 = cv2.add(image1,image2)
# add_img2 = cv2.add(image1 * alpha, image2 * beta)
# add_img2 = np.clip(add_img2, 0, 255).astype('uint8')
# add_img3 = cv2.addWeighted(image1,alpha, image2,beta,0)

# result_horizontal = np.hstack((image1,add_img3,image2))
# # cv2.createTrackbar("alpha","result", 0, 1)
# # cv2.createTrackbar("beta","result", 0, 1)

# cv2.imshow('add_img',result_horizontal)
# cv2.waitKey(0)

import numpy as np, cv2

# 영상 읽기
image1 = cv2.imread("./images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread("./images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")
# 트랙바의 콜백 함수
def nothing(x):
    pass

# 결과 이미지를 출력할 창 생성
cv2.namedWindow('dst')

cv2.createTrackbar('image1', 'dst', 0, 100, nothing)
cv2.createTrackbar('image2', 'dst', 0, 100, nothing)

while True:

    alpha = cv2.getTrackbarPos('image1', 'dst') / 100
    beta = cv2.getTrackbarPos('image2', 'dst') / 100

    # 이미지 합성
    result_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
    final_result = np.hstack((image1, result_img, image2))

    cv2.imshow('dst', final_result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()