import cv2
import numpy as np
import random

width, height = 640, 720
image = np.ones((height, width, 3), dtype=np.uint8) * 255


colors = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0)}

# for _ in range(5):

#     center = (random.randint(0, width), random.randint(0, height))
#     radius = random.randint(30, 100)
#     color = random.choice(list(colors.values()))
#     cv2.circle(image, center, radius, color, -1)

cv2.circle(image, (50,50), np.random.randint(30, 50), (0, 0, 255), -1)
cv2.circle(image, (300,70), np.random.randint(30, 50), (255, 0, 0), -1)
cv2.circle(image, (150,54), np.random.randint(30, 50), (0, 255, 0), -1)
cv2.circle(image, (400,400), np.random.randint(30, 50), (0, 0, 255), -1)
cv2.circle(image, (200,250), np.random.randint(30, 50), (255, 0, 0), -1)

cv2.imshow('Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("./origin.png",image)

def identify_color(bgr_value):
    if bgr_value == (0, 0, 255):
        return 'Red'
    elif bgr_value == (0, 255, 0):
        return 'Green'
    elif bgr_value == (255, 0, 0):
        return 'Blue'
    else:
        return 'Unknown'

# HoughCircles를 사용하여 원을 탐지
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=250, param2=10, minRadius=30, maxRadius=100)
print(circles)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]

        color = tuple(map(int, image[center[1], center[0], :]))

        cv2.rectangle(image, (center[0] - radius, center[1] - radius), (center[0] + radius, center[1] + radius), color, 1)
        cv2.putText(image, identify_color(color), (center[0] - radius, center[1] - radius - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


# 결과 이미지를 보여줍니다.
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()