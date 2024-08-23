from django.db import models
from datetime import datetime
import os

def user_directory_path(instance, filename):
    # 현재 날짜
    upload_date = datetime.now().strftime('%Y-%m-%d')
    # 파일의 확장자 추출
    ext = filename.split('.')[-1]

    # 필드 이름에 따라 디렉토리 설정
    directory_name = ""
    if hasattr(instance, 'question_4') and filename == instance.question_4.name:
        directory_name = 'Docker_Desktop_engine'
    elif hasattr(instance, 'question_7') and filename == instance.question_7.name:
        directory_name = 'Docker_Desktop_Window_Container_engine'
    elif hasattr(instance, 'question_8') and filename == instance.question_8.name:
        directory_name = 'Docker_Desktop_proxy'
    else:
        directory_name = 'others'

    # 이메일, 날짜, 필드명으로 파일 이름 생성
    filename = f"{instance.email}_{upload_date}_{directory_name}.{ext}"
    return os.path.join('uploads', directory_name, filename)

class SurveyResponse(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    question_1 = models.CharField(max_length=255)
    question_2 = models.CharField(max_length=255)
    question_3 = models.CharField(max_length=255)
    question_4 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    question_5 = models.TextField()
    question_6 = models.CharField(max_length=255)
    question_7 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    question_8 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    question_9 = models.CharField(max_length=255)
    question_10 = models.CharField(max_length=255)
    question_11 = models.CharField(max_length=255)
    question_12 = models.CharField(max_length=255)
    question_13 = models.CharField(max_length=255)

    @property
    def is_image_uploaded(self):
        return any([self.question_4, self.question_7, self.question_8])

    def __str__(self):
        return self.name


from django.db import models

class AdminUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'admin_user'  # 테이블 이름 지정
