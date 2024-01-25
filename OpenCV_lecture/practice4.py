import cv2
import numpy as np

# 데이터 생성
def create_circles(frame):
    red_circles = []
    blue_circles = []
    green_circles = []

    for _ in range(2):
        red_circles.append((np.random.randint(50, 590), np.random.randint(50, 430)))
        blue_circles.append((np.random.randint(50, 590), np.random.randint(50, 430)))
        green_circles.append((np.random.randint(50, 590), np.random.randint(50, 430)))

    for center in red_circles:
        frame = cv2.circle(frame, center, 30, (0, 0, 255), -1)

    for center in blue_circles:
        frame = cv2.circle(frame, center, 30, (255, 0, 0), -1)

    for center in green_circles:
        frame = cv2.circle(frame, center, 30, (0, 255, 0), -1)

    return frame, red_circles, blue_circles, green_circles

# 객체 탐지 및 인식
def detect_and_recognize(frame, red_circles, blue_circles, green_circles):

    for center in red_circles:
        x, y = center
        cv2.rectangle(frame, (x - 30, y - 30), (x + 30, y + 30), (0, 0, 255), 1)
        cv2.putText(frame, "Red", (x - 30, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    for center in blue_circles:
        x, y = center
        cv2.rectangle(frame, (x - 30, y - 30), (x + 30, y + 30), (255, 0, 0), 1)
        cv2.putText(frame, "Blue", (x - 30, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    for center in green_circles:
        x, y = center
        cv2.rectangle(frame, (x - 30, y - 30), (x + 30, y + 30), (0, 255, 0), 1)
        cv2.putText(frame, "Green", (x - 30, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    return frame


image = np.zeros((640,640,3),np.uint8)
image[:] = 255
title = 'chanyoung' #상태바 제목
image,red_circles, blue_circles, green_circles = create_circles(image)
detect_and_recognize(image,red_circles, blue_circles, green_circles)
cv2.imshow(title, image)



cv2.waitKey(0)                                       # 키 입력 대기
cv2.destroyAllWindows()                                   # 모든 윈도우 닫기
# 작업 완료 후 해제