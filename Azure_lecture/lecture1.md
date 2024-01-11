# Azure container 2024.01.11.
- labuser70@snuailab.onmicrosoft.com 
- !Seoul2025

- 리소스 그룹 70이 자신이 작업하는 공간이라고 보면 된다. 

- 1. 리소스 그룹 70으로 들어가서 <만들기> 클릭 -> market place 

- 2. Ubuntu를 market place에서 검색 Ubuntu 22.04 LTS(길게 지원하는 버전 long term support)

- 3. Ubuntu 22.04 LTS linux for the cloud 로 가상머신 만들기

- 서버로 들어오는 데이터 -> 인바운드 데이터 
- 서버에서 나가는 데이터 -> 아웃바운드 데이터 
- 4. 클라우드는 인바운드 옵션을 열어야한다, 왜냐하면 클라우드는 zero trust option이기 때문에, 기본적으로 접속을 막아놓고 시작한다. 

- 5. 가상머신에서 연결 -> 원시 SSH 연결 -> 연결 방법에 cmd line 복사 
- 6. local cmd로 cmd line 입력-> 실행 -> 가상머신 접속 

- 리눅스 명령어의 처음 $ 표시는 일반 유저, 관리자 권한은 # 으로 시작 

```
apt-get update # 패키지 업데이트
```
그냥 실행하면 관리자가 아니기 때문에 실행 에러 

super user do sudo를 추가해줘야함.

### 리눅스 기반 시작할 때 습관적으로 작성하는 명령어 2개 

```
sudo apt-get update 
```

```
sudo apt-get upgrade
```


``

### docker engine 가서 install 

- doc 따라서 docker 설치
- 설치 끝나면
```
sudo docker run hello-world
```

- docker sudo 없이 쓰는법
```
sudo usermod -aG docker <your_username>

logout

groups  # docker 가 추가됐는지 확인

docker run hello-world
```
- docker 기본 이미지 
```
docker pull ubuntu:18.04 # 우분투 이미지 다운로드 

docker images # 다운로드 받은 이미지들 모음 

docker ps # 현재 실행중인 이미지 목록

docker ps -a # 그 동안 실행했던 이미지 목록 
```

- 컨테이너 생성 및 접속 
```
# -it : interactive mode 이미지에 직접 들어가서 명령을 실행
# docker run -it -name <컨테이너 Name_tag> <image> <들어가서 실행할 커맨드>

docker run -it --name demo1 ubuntu:18.04 /bin/bash
# tip 
리눅스 옵션 명령어 줄 때, 약자 -n -i -t 는 대시 1개 '-' 
풀네임 --name 으로 할 때는 -- 대시 두개 
```

- 접속 종료 
```
# -it > interactive mode 접속 종료  
exit

# 접속 종료 이후에도 계속 컨테이너를 실행하도록 하는 옵션 demon (메모리에 항상 떠있는건 거의 -d 옵션)
docker run -it -d --name demo2 ubuntu:18.04
# 실행 시키면 컨테이너 고유 번호 나옴 
#(60717a6901ca0345d925cf2a65825a0f10fb53bf98c4ed51818ef1eea070b0ec)
```
- 실행중인 컨테이너에 접속하는 방법  execute
```
docker exec -it demo2 /bin/bash #demo2 컨테이너의 interactive mode로 접속

# -it 없이 하면 어떻게 하나 ? 
# /bin/bash 설정 안하고 접속해서 bash 실행 어떻게 하나? 
```
- shell 명령어 -c "while ture; do $(echo date); sleep 1;"
- -c 는 sh에서 사용할 커맨드를 정의하기 위해 옵션을 붙인다. 
```
docker run --name demo3 -d busybox sh -c "while ture; do $(echo date);sleep 1;"

#1초마다 현재 시각을 출력하는 컨테이너 유령모드로 실행
```
- 컨테이너 log 찍기 
```
docker logs demo3 
```

- 컨테이너 종료 및 제거 
```
docker stop demo3 # 종료
docker rm demo3 #제거 
docker rm -f demo3 # 종료 후에 제거 
```

- 종료한 컨테이너를 다시 실행 
```
docker start demo3 
```

- docker iamge를 지우는 명령 
```
docker rmi <image name> 
```

## Docker image 만들기 (dockerization)
- docker file 만들기 (docker file에 필요한 내용을 세팅) 
    - docker 이미지는 단순히 운영체제만 들어가는게 아니라, 애플리케이션 또는 코드만이 아니라 어플리케이션과 dependent한 모든 것을 패키징한 데이터  

### Setting 

```
cd $HOME
pwd

#디렉토리 만들기 
mkdir docker-practice
cd docker-practice

# docker file 생성 
touch Dockerfile
# 파일 내용 보기 
cat Dockerfile 

# image를 만들기전에 베이스 image를 설정 
# FROM <image>:tag AS <name>
# AS 는 엘리아싱 이미지 이름 짧게 부르겠다 numpy as np 랑 같은 의미 
FROM ubuntu:18.04 # ubuntu18.04를 베이스 이미지로 삼는다. 

# COPY <file a> /directory/<file b> 
COPY a.txt ./practice/b.txt # a file을 b로 복사해서 이미지를 만들어라 

# RUN <code>
RUN pip install torch
RUN pip intall -r requirements.txt 

# CMD 명시한 커맨드를 도커 컨테이너가 시작될 때, 실행하는 것을 명시하는 명령어 
# 하나의 도커 이미지에서는 하나의 CMD만을 사용할 수 있다. 
CMD python main.py #주로 메인 실행

# WORKDIR  컨테이너 내부에서 주로 사용할 디렉토리 세팅

# ENV  컨테이너 내부에서 주로 사용할 환경변수 세팅


# EXPOSE 컨테이너에서 열어줄 포트 프로토콜 지정할 수 있다 .
# 프로토콜 디폴트 TCP 
# 포트 안열면 다 막혀있음 

# 만들어낸 도커 파일을 이미지로 만드는 명령 build 
# docker build -t my-image:v1.0.0 <이미지를 저장할 위치>
# -t 이미지 태그 지정 예시에서는 my-image:v1.0.0 

docker build -t my-image:v1.0.0 . # 현재 위치 

#build 하면 도커 시스템안에 이미지 들어와있음. 
docker run my-image:v1.0.0
docker run -it --name demo1 my-image:v1.0.0
```
### Docker Registry (도커 이미지 저장소)
- docker registry 실행
- local host 5000으로 할당해서 레지스트리와 통신 가능 
```
#registry 이미지가 registry이름으로 생성
docker run -d -p 5000:5000 --name registry registry
```
- my-image를 방금 생성한 레지스트리를 바라보도록 태그
```
#내가 만든 이미지를 localhost 5000으로 레지스트리와 연결된 my-image:v1.0.0으로 태그한다.
docker tag my-image:v1.0.0 localhost:5000/my-image:v1.0.0
```
> 이렇게 태그를 하면 처음에 생성한 my_image가 있고, local_host로 연결된(링크된)  my_image가 있다. <br>
실제로 이미지가 새로 생긴거는 아니고 링크만 된 것 
<br>
> 링크만 되어 있고 파일이 docker hub에 올라가 있지는 않다.

- my-image를 레지스트리에 push (업로드)
```
docker push localhost:5000/my_image:v1.0.0
```

- [Docker Hub](https://hub.docker.com/)  (docker github)

- docker hub에서 이미지 가져다쓰기 또는 레포에 올리기 
```
- docker login 
```
```
docker login #docker hub의 username 입력 후 패스워드 입력 
```
- 연결 후 태깅해서 push 하면 바로 나의 레포로 날아감. 
```
docker tag my_image:v1.0.0 chanyoun/my_image:v1.0.0
```

```
docker push chanyoun/my_image:v1.0.0
```