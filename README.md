# 폐쇄망 환경 docker 컴플라이언스 수립에 필요한 survey 애플리케이션

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

## 📋 구성
이 프로젝트는 docker 사내 컴플라이언스를 결정하는 Django 기반 웹 애플리케이션입니다. 주요 구성 요소는 다음과 같습니다:

- **Django**: Python 웹
- **PostgreSQL**: 데이터베이스 
- **Docker**: 애플리케이션 컨테이너
- **Docker-Compose**: 컨테이너 동시 실행
- **Minio**: 이미지 저장소
![image](https://github.com/user-attachments/assets/4d5d5eae-1921-4998-93c8-1ea973cccc7c)


## 🔄 Model 변경 시 Migration 방법

모델 변경 시 데이터베이스 스키마를 업데이트하기 위해 마이그레이션을 수행해야 합니다. 아래 단계에 따라 진행하세요:

1. python manage.py makemigrations
2. docker-compose down -v
3. docker-compose up --build

## 🚀 어디서든 실행 하는법

1. 자신의 환경에서 
[anywhere-excute-file/docker-compose.yml](https://github.com/limsangwoons/docker-compliance-survey/blob/main/anywhere-excute-file/docker-compose.yml) 
해당 파일 복사 docker-compose.yml에 저장
2. docker compose up 실행
3. ⚠️ 주의 사항 : 최신 이미지 적용 시 기존 이미지 삭제 



## 🌐 실행 화면
### Survey 화면
![image](https://github.com/user-attachments/assets/86c0efc4-3df4-4cec-9720-a4abc67f93b4)
