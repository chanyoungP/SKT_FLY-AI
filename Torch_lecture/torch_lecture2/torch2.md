# Lecture 2 torch 

## Neural Network for image classification 
- 이미지 분류 
- 객체 인식
- 이미지 분할 

## image classification 

### LeNet-5 

LeNet-5는 두 개의 컨볼루션 레이어와 두 개의 서브샘플링 레이어를 가지고 있습니다.
컨볼루션 레이어에서는 입력 이미지의 특징을 감지하고 서브샘플링 레이어에서는 이미지의 크기를 줄여 연산을 효율적으로 만듭니다.


### AlexNet 
AlexNet의 합성곱층에서 사용된 활성화 함수는 ReLU 이다. 


### VGGNet 
모든 합성곱 커널의 크기는 3x3 
풀링 커널의 크기는 2x2  스트라이드 2

피쳐맵 사이즈를 유지하면서 채널만 늘려가다가 줄일 때는 맥스풀링만으로 크기를 줄인다. 


### 1x1 conv 는 채널 selection 느낌

## MMDetection 오픈 소스 라이브러리 