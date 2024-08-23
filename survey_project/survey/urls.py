from django.urls import path
from . import views

urlpatterns = [
    path('create-admin/', views.create_admin_user, name='create_admin'),
    path('result/', views.result_view, name='result_view'),
    path('result/dashboard/', views.result_dashboard, name='result_dashboard'),
    path('download/', views.download_excel, name='download_excel'),
    path('download/json/', views.download_json, name='download_json'),
    path('', views.survey_view, name='survey'), 
]
