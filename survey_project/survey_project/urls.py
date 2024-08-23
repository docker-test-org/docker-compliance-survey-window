from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/', include('survey.urls')),  # survey 앱의 URL 포함
    path('', lambda request: redirect('/survey/')),  # 기본 경로로 접근 시 설문조사로 리디렉션
]
