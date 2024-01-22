# Lecture 1 : Pytorch 

## What is pytorch ? 

### overview 

- 루아 언어로 개발되었던 토치를 페이스북에서 파이썬 버전으로 내놓은 것. 
- GPU 연산 속도를 빠르게 하는 역할
- 기울기를 계산할 때, 빠른 계산이 가능

### torch.autograd : 자동 미분 패키지
> 연산 그래프의 동적 설계를 가능하게 하는 패키지 

### torch.nn : 신경망 패키지 
> nn.Conv 등 신경망 구조를 설계할 때, 필요한 연산들을 사용할 수 있는 패키지

### torch.multiprocessing :  분산할당 패키지
> GPU 2개 쓰거나 메모리 분산 할당할 때 사용하는 패키지 


### torch.utill : 데이터로더 등 다양한 유틸 패키지 
 

## torch 기초 문법

### 텐서 다루기 
- 텐서 생성 및 변환 
```
import torch
torch.tensor([[1,2],[3,4]]) #2차원 형태의 텐서 생성
torch.tensor([[1,2],[3,4]],device ="cuda:0") # GPU에 텐서 생성
torch.tensor([[1,2],[3,4]],dtype = torch.float64) # dtype을 이용하여 텐서 생성 
```
- 텐서를 ndarray로 변환

```
torch.tensor([[1,2],[3,4]]).numpy()

#
temp = torch.tensor([[1,2],[3,4]],device ="cuda:0")
temp.to("cpu").numpy() # GPU 상 텐서를 CPU로 보내주고 numpy로 변환 

```

- 텐서의 차원을 조작하는 코드 
```
temp = torch.tensor([
    [1,2],
    [3,4]
])

temp.shape
temp.view(4,1) # 2x2 행렬을 4x1로 변환
temp.view(-1) # 2x2 행렬을 1차원 벡터로 변환
temp.view(1,-1) # 2x2 -> 1x4로 변환  -1은 나머지 알맞게 변환해라 
temp.view(-1,1) # -> 4x1 
```


### 데이터로 다루기 

- Pandas로 데이터 호출하기 

```
import pandas as pd
import torch

data = pd.read_csv(<data path>)
x = torch.from_numpy(data['x'].values).unsqueeze(dim=1).float()
y = torch.from_numpy(data['y'].values).unsqueeze(dim=1).float()
```
> unsqueeze : (224,224,3).unsqueeze(dim=1) -> (1,224,224,3) 

- 데이터 준비 (커스텀 데이터셋을 만들어서 사용)
- 딥러닝은 기본적으로 대량의 데이터를 이용하여 모델을 학습
- 데이터를 한 번에 메모리에 불러와서 훈련시키면 시간과 비용 측면에서 효율적이지 않음
- 데이터를 한 번에 다 부르지 않고 조금씩 나누어 불러서 사용하는 방식이 커스텀 데이터셋(custom dataset)

- 1. Class 구성
```
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self):
    def __len__(self):
    def __getitem__(self,index):

```

- 커스텀 데이터셋 class 구성 예제 
```
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.label = pd.read_csv(csv_file)

    def __len__(self):
        return len(self.label)

    def __getitem__(self,index):
        sample = torch.tensor(self.label.iloc[idx,0:3]).int()
        label = torch.tensor(self.label.iloc[idx,3]).int()
        return sample, label
```

- 사용 예제 
```
tensor_dataset = CustomDataset('csv_file')

# DataLoader는 직접 모델에 배치 사이즈만큼 가져다주는 개체 
dataset = DataLoader(tensor_dataset,batch_size = , shuffle = True) 
```
> torch.utils.data.DataLoader
  - 데이터로더(DataLoader) 객체는 학습에 사용될 데이터 전체를 보관했다가 모델
학습을 할 때 배치 크기만큼 데이터를 꺼내서 사용
  - 이때 주의할 것은 데이터를 미리 잘라 놓는 것이 아니라 내부적으로
반복자(iterator)에 포함된 인덱스(index)를 이용하여 배치 크기만큼 데이터를
반환한다는 것

> Dataset과 Dataloader를 잘 구분해서 생각해야한다. Dataset은 직접 짜야하는 부분이 많다, 하지만 Loader는 set class의 구조만 지키면 loader 는 사용하기만 한다. 

### 데이터 준비 완성 예제 
```
import torchvision.transforms as transforms

mnist_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,),(1.0,))
])

from torchvision.datasets import MNIST
import requests
download_root = './'
train_dataset = MNIST(download_root, transform = mnist_transform, train = True, download=True)
valid_dataset = MNIST(download_root, transform = mnist_transform, train = False, download=True)
test_dataset = MNIST(download_root, transform = mnist_transform, train = False, download=True)

```

### 모델 정의 
- nn.Module()을 상속하여 정의
- 따라서 기본적으로 모델 클래스에는 init()과 forward()함수를 포함 
- init에서는 모델에서 사용할 모듈을 정의하고 forward()함수에서는 모델에서 실행되어야할 연산을 정의 

```
class MLP(nn.Module):
    def __init__(self,inputs):
        super(MLP,self).__init__()
        self.layer = nn.Linear(inputs,1)
        self.activation = nn.Sigmoid()

    def forward(self,X):
        X = self.layer(X)
        X = self.activation(X)
        return X
```


- Sequential 로 정의할 수 있다. 

```
class MLP(nn.Module):
....
self.layer1 = nn.Sequential(
    nn.Conv2d
    nn.ReLU
    nn.MaxPool2d 
)

self.layer2 = nn.Sequential(
    ...
)

def forward( ..) :
    x = self.layer1(x)
    x = self.layer2(x)
    return x 
```

## 모델의 파라미터 정의 
- 모델을 학습하기 전에 필요한 파라미터를 정의 

### Loss function 
> 정답과 얼마나 틀렸는지 계산

### optimizer 
> 정답에 가까워지기위해서 어디로 어떻게 가야할지를 계산

### scheduler 
> 방향이 정해지면 얼마나 건너갈지 정함. 

```
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.001, momentum = 0.9)
scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer = optimizer,lr_lambda = lambda epoch : 0.95**epoch))


학습 코드 
for i in range(epoch):
    ...
```


### 학습

```
optimizer.zero_grad()
# optimizer 초기화 (기존 파라미턱값을 가지고 있으니까 버리도록한다.)

compute loss
optimizer.step
scheduler.step 

```

### 모델 평가 
- import torchmetrics 
```
torchmetrics.Accuracy() 

```

### 훈련 과정 모니터링 
model.train()
model.eval() 
