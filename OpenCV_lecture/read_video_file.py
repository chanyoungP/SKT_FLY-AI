import cv2
import numpy as np

# 카메라 연결
cap = cv2.VideoCapture(0)

# 관심 영역 좌표 및 크기
roi_x, roi_y, roi_width, roi_height = 200, 100, 100, 200

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 관심 영역 설정
    roi = frame[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]

    # 녹색 성분 증가
    roi[:, :, 1] = np.clip(roi[:, :, 1] + 50, 0, 255)

    # 빨간색 테두리 표시
    cv2.rectangle(frame, (roi_x, roi_y), (roi_x+roi_width, roi_y+roi_height), (0, 0, 255), 3)

    # 화면에 출력
    cv2.imshow('Camera Feed', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 작업 완료 후 해제
cap.release()
cv2.destroyAllWindows()
