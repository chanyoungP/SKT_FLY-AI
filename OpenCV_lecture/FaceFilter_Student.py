import cv2
import numpy as np

def preprocessing(file_path):
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image, gray

def get_rot_angle(centers):

    return angle

def correct_image(image, face_center, eye_centers):
    angle = get_rot_angle(eye_centers)
    rot_mat = cv2.getRotationMatrix2D(face_center, angle, 1)

    size = image.shape[1::-1]
    corr_image = cv2.warpAffine(image, rot_mat, size, cv2.INTER_CUBIC)

    eye_centers = np.expand_dims(eye_centers, axis=0)

    corr_centers = cv2.transform(eye_centers, rot_mat)
    corr_centers = np.squeeze(corr_centers, axis=0)

    return corr_image, corr_centers, angle

# 정면 얼굴 검출기 불러오기
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
# 눈 검출기 불러오기 
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

# 투명도가 포함된 얼굴 이미지 불러오기
image, gray = preprocessing("./images/example.jpg")

if image is None:
    raise Exception("영상 파일 읽기 에러")

# 얼굴 검출하기
height, width, _ = image.shape
faces = face_cascade.detectMultiScale(gray)

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
# cv2.imshow("image", image) # 얼굴 부분 표시 후 보여주기
# cv2.waitKey(0)
i = 0
for face in faces:
    x, y, w, h = face
    # 얼굴 부분만 가져오기
    face_image = image[y:y+h , x:x+w]

    # 눈 검출하기
    eyes = eye_cascade.detectMultiScale(face_image)
    
    if len(eyes) == 2:
        face_center = (int(x+w//2), int(y+h//2))
        # 각 눈의 좌표 계산
        eye_centers = [(ex+ew//2+x, ey+eh//2+y) for ex, ey, ew, eh in eyes]
        # for eye_center in eye_centers:
        #     cv2.circle(image, eye_center, 10, (0, 255, 0), 2)

        # 두 눈 좌표간 각도 계산
        angle = np.degrees(np.arctan2(eye_centers[1][1]-eye_centers[0][1], eye_centers[1][0]-eye_centers[0][0]))

        # 두 눈 사이 중앙 좌표 계산
        eye_center = ((eye_centers[0][0]+eye_centers[1][0])//2, (eye_centers[0][1]+eye_centers[1][1])//2)

        # 안경 이미지 불러오기
        glasses, glasses_gray = preprocessing("./images/glasses.png")
        
        # 안경 이미지와 얼굴의 비율을 맞춤
        glasses_h, glasses_w, _ = glasses.shape
        ratio = w / glasses_w
        new_size = (int(glasses_w*ratio), int(glasses_h*ratio))
        resized_glasses = cv2.resize(glasses, dsize=new_size, interpolation=cv2.INTER_AREA)

        resized_h, resized_w, _ = resized_glasses.shape
        glasses_center = (resized_h//2, resized_w//2)
        
        # 안경 이미지 회전
        rot_mat = cv2.getRotationMatrix2D(glasses_center, -angle, 1)
        corr_glasses = cv2.warpAffine(resized_glasses, rot_mat, (resized_w, resized_h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
        
        # 안경 이미지를 반영함
        for y in range(corr_glasses.shape[0]):
            for x in range(corr_glasses.shape[1]):
                # 눈 중앙 위치와 안경 사진의 중앙 위치를 맞추기 위한 좌표 계산
                y2 = eye_center[1] - glasses_center[1] + y
                x2 = eye_center[0] - glasses_center[0] + x
                # 안경 이미지의 크기나 전체 이미지의 얼굴 위치가 구석에 쏠려 있는 경우
                #   반영될 안경 이미지가 전체 이미지의 범위를 벗어날 수 있음
                if 0 <= x2 < width and 0 <= y2 < height:
                    if np.all(corr_glasses[y, x, :] != [0, 0, 0]):
                        image[y2, x2, :] = corr_glasses[y, x, :]
    else:
        print("눈 미검출")

    # cv2.rectangle(image, faces[0], (255, 0, 0), 2)
    
    # image, center, angle = correct_image(image, face_center, eye_centers)

cv2.imshow("image", image)
cv2.waitKey(0)