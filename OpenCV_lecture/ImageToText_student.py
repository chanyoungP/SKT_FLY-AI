import cv2
import numpy as np
import pytesseract


TESSERACT_PATH = "C:/Program Files/Tesseract-OCR/tesseract.exe" #테서렉스 설치 경로
imgpath='./images/2.jpg'  #이미지 파일 경로
win_name = "Image To Text"  #OpenCV 창 이름
img = cv2.imread(imgpath)   #이미지 읽어오기


# # 원본 이미지 크기 얻기
# height, width = img.shape[:2]

# # 윈도우 크기 지정
# window_width = 800
# window_height = int(height * (window_width / width))
# img = cv2.resize(img, (window_width, window_height))


draw = img.copy()
pts_cnt = 0
pts = np.zeros((4,2),dtype=np.float32)

#마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global pts_cnt
    global img

    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(draw,(x,y),10,(0,255,0),-1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x,y]
        pts_cnt += 1
        if pts_cnt == 4:
            sm = pts.sum(axis = 1)
            diff = np.diff(pts,axis = 1)

            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]

            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            w1 = abs(bottomRight[0] - bottomLeft[0])
            w2 = abs(topRight[0] - topLeft[0])
            h1 = abs(topRight[1] - bottomRight[1])
            h2 = abs(topLeft[1] - bottomLeft[1])
            width = max([w1,w2])
            height = max([h1,h2])

            pts2 = np.float32([[0,0], [width-1,0],[width-1, height-1],[0,height-1]])

            mtrx = cv2.getPerspectiveTransform(pts1,pts2)
            result = cv2.warpPerspective(img, mtrx,(int(width), int(height)))
            cv2.imshow('scanned', result)
            img = result
    return 0


#이미치 처리 함수
def ImgProcessing():
    global img
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    norm_img = np.zeros((img.shape[0],img.shape[1]))
    img = cv2.normalize(img,norm_img,0,255,cv2.NORM_MINMAX)

    img = cv2.GaussianBlur(img,(3,3),0)

    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imshow('testing',img)

    #png save 
    cv2.waitKey(0)
    cv2.imwrite('./images/processing.png',img)

    return img


#OCR 함수
def GetOCR():
    #이미지 불러오기
    global img
    results = []

    #OCR모델 불러오기
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    #OCR모델로 글자 추출
    text = pytesseract.image_to_string(img, lang='kor+eng')
    
    return text


cv2.imshow(win_name,img)
cv2.setMouseCallback(win_name,onMouse)
cv2.waitKey(0)
img = ImgProcessing()
cv2.waitKey(0)

text = GetOCR()
print(text)          #입력 대기
