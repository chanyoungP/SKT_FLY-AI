# Cloud computing

## Keyword of cloud computing 

### 1. computing

### 2. networking

### 3. storage

## 공동 책임 모델
- 클라우드는 다 같이 쓰기 떄문에 책임 모델이 필요하다. 
### SaaS
- Software as a Service
> 인터넷으로 접근 가능, Google Workspace, Microsoft 365 ...

### PaaS
- Platform as a Service
> 응용 프로그램을 개발, 테스트, 배포 관리하기 위한 플랫폼을 제공
<br> 하드웨어, 운영체제 네트워크 관리 등을 클라우드 공급자가 처리
<br> Google App Engine, MS Azure App Service

### IaaS
- Infrastructure as a Service
> 가상화된 컴퓨팅 리소스를 제공하는 모델, 사용자는 가상 머신, 스토리지, 네트워크 등을 필요에 따라 프로비저닝(가상화한다.), 사용자는 운영체제 미들웨어 애플리케이션을 스스로 관리해야한다.
<br> Amazon EC2, MS Azure VM , Google Compute Engine 

## 사용량 기반 모델
- 클라우드는 리소스를 __사용한만큼__ 비용을 지불한다.

## Azure 워크 플로우 

### 1. 리소스 그룹 만들기
- 그룹 선언

### 2. 관리 디스크 만들기
- SSD 만들기 

### 3. 터미널 열기 (스토리지 없으면 스토리지 생성)
```
atoz89961 [ ~ ]$ az account list -o table

atoz89961 [ ~ ]$ az resource list -o table

```

### 4. 터미널에서 디스크 생성 
```
New-AzDiskConfig `
>> -Location $location `
>> -CreateOption Empty `
>> -DiskSizeGB 32 `
>> -Sku Standard_LRS
PS /home/atoz89961> $diskName = 'edu_ps_disk'  
PS /home/atoz89961> New-AZDISK -ResourceGroupName $rgName -DiskName $diskName -Disk $DiskConfig

```
### 5. ARM template 


```
# 리소스 그룹 삭제 
az group delete --name <groupname> --no-wait --yes

#디스크 삭제 명령
az disk delete --name edu_ps_disk --resource-group edu_destination
``` 


### 리소스 그룹 생성하고, 스토리지 어카운트 생성
```
atoz89961 [ ~ ]$ az group create --name MyResourceGroup --location eastus

atoz89961 [ ~ ]$ az storage account create --name mystgacc99 --resource-group MyResourceGroup --location eastus --sku Standard_LRS
```