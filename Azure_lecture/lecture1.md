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

# 접속 종료 이후에도 계속 컨테이너를 실행하도록 하는 옵션 

```