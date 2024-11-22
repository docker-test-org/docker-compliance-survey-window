# Docker Compliance Survey Application (Window)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

## 📋 Overview
This project is a Django-based web application designed to establish Docker compliance within a corporate environment. The main components include:

- **Django**: Python web framework
- **PostgreSQL**: Database 
- **Docker**: Application containerization
- **Docker-Compose**: Simultaneous container execution
- **Minio**: Image storage solution
![image](https://github.com/user-attachments/assets/4d5d5eae-1921-4998-93c8-1ea973cccc7c)


## 🔄 How to Migrate After Model Changes

When models are changed, a migration is required to update the database schema. Follow these steps::

1. Run python manage.py makemigrations
2. Run docker-compose down -v
3. Run docker-compose up --build

## 🚀 How to Run Anywhere

1. Copy the file from
[anywhere-excute-file/docker-compose.yml](https://github.com/limsangwoons/docker-compliance-survey/blob/main/anywhere-excute-file/docker-compose.yml) 
and save it as docker-compose.yml in your environment.
2. Execute docker compose up
3. ⚠️ Note: When using the latest image, delete the existing image before applying the new one.



## 🌐 Application Screens
### Survey Screen
![image](https://github.com/user-attachments/assets/86c0efc4-3df4-4cec-9720-a4abc67f93b4)


