# Cloud Lecture 5 : Azure Cosmos Database 

## Standard RDB 
- DB
- Table
- Columns

## Core DB 구성 요소

### Database Account
- 데이터베이스 서버의 의미 
- 서버가 있어야 인스턴스로 데이터베이스를 만들 수 있다. 

### Container 
- 데이터베이스는 컨테이너로 이루어져 있음. 각각의 컨테이너 안에 item들이 JSON 형태로 이루어짐.

### Items
- JSON 형태


## Azure Cosmos DB for MongoDB 
- 기본 JSON 형태 

### Azure Cosmos 실습

-Azure shell 리소스 그룹 생성 
```
atoz89961 [ ~ ]$ resourceGrp="mycosmosdbmongo-cy-rg"
atoz89961 [ ~ ]$ location="eastus"
atoz89961 [ ~ ]$ cosmosdbAccount="mycosdbcy"
atoz89961 [ ~ ]$ az group create --name $resourceGrp --location $location

```
- Azure  cosmosDB 어카운트 생성하면서 MongoDB 만들기 
```
atoz89961 [ ~ ]$ az cosmosdb create --name $cosmosdbAccount --resource-group $resourceGrp --locations regionName=$location --kind MongoDB
```
- cosmosDB 연결하려는 키 뽑아오기
- MongoDB 연결 문자열(connection string)은 MongoDB 서버와의 연결을 설정하기 위한 문자열입니다. 이 문자열은 MongoDB 서버의 주소, 포트, 인증 정보, 데이터베이스 이름 등과 관련된 정보를 포함합니다.
```
atoz89961 [ ~ ]$ az cosmosdb keys list --type connection-strings --resource-group $resourceGrp --name $cosmosdbAccount
```

- cosmosdb 연결해서 사용
1. cosmosmongo 폴더 하나 만들고 vs code로 열기
```
# vs code 터미널로 가상환경 세팅
python -m venv venv 

pip install pymongo python-dotenv

# .env파일 생성

# 파이썬 파이 생성 후 실행 연결 

# 값 추가하고 삭제 업데이트 예제 파일 참고 

```

## Azure Database for Postgre SQL 

### MySQL 
- 현재는 Azure Database for MySQL flexiable server 로 할 수 있는데. 각 지역에서 생성이 될지 모른다. 

> Azure database for mysql 유연한 서버 선택 - 만들기 - 리소스 그룹 만들기 - 서버 이름 생성 - 워크로드 유형 선택 
> - 인증방법 MySQL 인증만 선택 - 관리자 사용자 이름 선택 - 방화벽 규칙 아이피 추가 
>
> MySQL workbench 다운로드 > azure 데이터베잇, SSL pem 파일 다운로드 -> workbench 실행 -> + 버튼 -> 이름에 db 서버 이름 -> 아이피 서버 이름 복붙 
> -> 호스트 이름 설정 애저랑 같은걸로 -> pem file 설정  test 커넥션 확인 연결 
>
> mysql 들어가서  ``` create database sample_db ``` 로 데이터베이스 생성 


## Azure machine learning studio 작업 영역 및 기본 설정 

### 실습 
- 작업영역
  > azure machine learning 최상위 영역 
[- ht](https://ml.azure.com/home?tid=fd02e20e-0ff3-4c05-98e2-ca7c15b5031b)
> 작업 영역 만들고 
- 컴퓨터 인스턴스 만들기 
  > 머신러닝 전용 가상머신 만든다는 의미 

### TTS 서비스 구현 
- Speech API 
> 음성 리소스 만들기 : azure speech service 들어가서 새로 만들기
> TTS 폴더 만들기 - 파이썬 파일 만들기 -```pip install python-dotenv azure-congnitiveservice-speech```
> 
> 키, 지역 코드 복사 
> 코드에 키 지역 코드 넣고  Azure Cognitive Services Speech SDK 사용하여 파이썬 코드 작성 실행 TTS 파일 참고 


### 번역 서비스 구현 
> azure 포탈에서 번역가 검색 
> 리소스 생성
> key location, endpoint 확인 endpoint 는 <웹 API> 탭에서 하고 싶은 번역 복사 (텍스트 번역, 문서 번역) (실습에서는 문서 번역) 
> 파이썬 코드에서 env 설정에서 키 값 설정하고 , requirements.txt 파일 pip install 
> tans.py 작성 
> 