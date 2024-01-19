# Cloud lecture 4 

## 배포 슬롯 
> 배포 슬롯은 자체 호스트 이름을 가진 라이브 앱
>
> 앱 서비스 계획을 사용하는 경우에만 슬롯 제공
>
> 앱 컨텐츠 및 구성은 프로덕션 슬롯과 다른 슬롯 간에 교환 가능
>
> 새로운 기능을 프로덕션 슬롯이 아닌 다른 슬롯에 배포할 경우 애플리케이션의 변경 사항에 대한 유효성 검사 가능
>
> 슬롯으로 앱을 배포하고 프로덕션으로 교환하기 때문에 프로덕션으로 교환되기 전에 슬롯에 있는 모든 인스턴스가 준비된 상태로 애플리케이션 배포시 가동 중지가 발생하지 않음. 
>
"순차적으로 업데이트할 수 있다는 의미" 


## 실습
1. 웹앱 생성
2. 로컬 git repo를 이용한 git 배포 구성
3. git client 구성 및 웹앱 소스코드 복제
4. production 슬롯에 앱을 배포하도록 git remote구성
5. 새 staging 슬롯 생성
6. 새 stagint 슬롯에 git 배포 구성
7. 앱 소스코드 수정 및 staging 슬롯에 배포
8. 슬롯 구성 및 교환 

## 도커 컨테이너 인스턴스 

### 간단한 실습 
> 1. 만들기
> 2. 이름 및 정보 추가 이미지 빠른 시작 이미지 
> 3. 검토 만들기 
> 4. 퍼블릭 아이피 복사 검색 
>

## 도커, 도커 허브 ACR

### 도커 구조
- 도커 클라이언트
> 도커 명령어를 입력하는 클라이언트
- 도커 데몬
> 도커 클라이언트로부터의 도커 API 요청을 수신 처리 
- 도커 엔진

- 도커 호스트
- 도커 레지스트리

### 도커 이미지 
> 여러 계층으로 이루어진 이진 파일 
> 컨테이너를 생성하고 실행할 때 사용됨
> 일반적으로 도커 허브 저장소에서 검색 후 다운로드 

> docker pull <image:tag>

> docker file -> build -> image -> run -> container


### 도커 실습
1. 가상머신 만들기 
2. 도커 설치
3. hello-world 이미지 run 

```
docker pull node:20-alpine

docker run -it -d -p 8080:8080 --name nodejs_app node:20-alpine

docker ps
```

```
docker pull nginx:1.25.3-alpine

docker run --name nginx-srv -p 80:80 -d nginx:1.25.3-alpine
```

```
#웹 앱 실행중이므로 가상 머신 공용 아이피로 접근 가능 

#단, vm HTTP 80 인바운드 포트 규칙 추가해줘야함.. .

```

- 여기까지가 docker 컨테이너를 이용한 웹 서비스 접근 방법 

> 로컬 VM 컨테이너 사이에서 처음 컨테이너 만들 때, VM하고 컨테이너 사이 포트 80 열어주었고, 로컬과 VM 사이를 인바운드 규칙 추가로 따로 적용을 해줘야한다. 
>
> 브라우저에서 공용아이피로 접근할 때, 우리는 로컬 -> VM -> 컨테이너 로 접근한다. 


### 도커 파일 만들고 업로드하기 

```
vi Dockerfile 

#파일 편집 

# 도커 빌드해서 이미지로 만들기
 
# 이미지 실행해서 컨테이너로 실행 docker run 


#마운트해서 하기 
sudo docker run --name apache -p 80:80 -d -v /home/chanchan/edupicker/html:/var/www/html apache2:1.0
```

### ACR : Azure Container Registry 

```
# Azure CLI bash  
# ACR은 도커 허브  Azure 버전 
az acr create --name mycyregi99 --resource-group edu-docker-cy --sku standard --admin-enabled true




```

### ACI Azure container instance 
- 인스턴스를 생성해서 version 관리하고 웹으로 바로 배포 가능 


## Azure Cosmos DB -SQL 및 CRUD  

### Cosmos DB
- 하이브리드 JSON 형식도 쓸 수 있고, 정통 SQL 형식도 쓸 수 있음. 


### Azure cosmos DB 사용하기
1. 코스모스 디비 만들기
2. 데이터베이스와 컨테이너 추가하기
3. 




