from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BasicInfoForm, SurveyQuestionsForm
from .models import SurveyResponse
import openpyxl
from datetime import datetime
from django.shortcuts import render, redirect
from .models import AdminUser
from .forms import AdminLoginForm
from .forms import AdminUserCreationForm
from collections import Counter
import json

# 설문 폼을 처리하는 뷰
def survey_view(request):
    button_text = None  # 변수 초기화

    if request.method == 'POST':
        if 'step' not in request.session:
            request.session['step'] = 1

        if request.session['step'] == 1:
            form = BasicInfoForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']

                # 이미 설문을 제출한 사용자인지 확인
                if SurveyResponse.objects.filter(email=email).exists():
                    # 자바스크립트 알림을 띄우도록 템플릿에 전달
                    return render(request, 'survey/survey_form.html', {
                        'form': form,
                        'button_text': "Next",
                        'email_exists': True  # 이메일 중복 플래그 전달
                    })
                request.session['response_data'] = {
                    'name': form.cleaned_data['name'],
                    'position': form.cleaned_data['position'],
                    'title': form.cleaned_data['title'],
                    'phone_number': form.cleaned_data['phone_number'],
                    'email': form.cleaned_data['email'],
                }
                request.session['step'] = 2
                return redirect('survey')
            else:
                print(form.errors)  # 폼 오류 출력
            button_text = "Next"  # Step 1에서 button_text 설정

        elif request.session['step'] == 2:
            form = SurveyQuestionsForm(request.POST, request.FILES)
            if form.is_valid():
                response_data = request.session.get('response_data')

                response = SurveyResponse(
                    name=response_data['name'],
                    position=response_data['position'],
                    title=response_data['title'],
                    phone_number=response_data['phone_number'],
                    email=response_data['email'],
                    question_1=form.cleaned_data['question_1'],
                    question_2=form.cleaned_data['question_2'],
                    question_3=form.cleaned_data['question_3'],  
                    question_4=form.cleaned_data['question_4'],  
                    question_5=form.cleaned_data['question_5'],
                    question_6=form.cleaned_data['question_6'],  
                    question_7=form.cleaned_data['question_7'],
                    question_8=form.cleaned_data['question_8'],
                    question_9=form.cleaned_data['question_9'],  
                    question_10=form.cleaned_data['question_10'],  
                    question_11=form.cleaned_data['question_11'],
                    question_12=form.cleaned_data['question_12'],  
                    question_13=form.cleaned_data['question_13'], 
                )
                response.save()

                del request.session['step']
                del request.session['response_data']

                return render(request, 'survey/thank_you.html')
            else:
                print(form.errors)  # 폼 오류 출력
            button_text = "Submit"  # Step 2에서 button_text 설정

    else:
        if 'step' in request.session and request.session['step'] == 2:
            form = SurveyQuestionsForm()
            button_text = "Submit"
        else:
            form = BasicInfoForm()
            request.session['step'] = 1
            button_text = "Next"

    if button_text is None:
        raise ValueError("button_text가 초기화되지 않았습니다. 로직을 확인하세요.")

    return render(request, 'survey/survey_form.html', {'form': form, 'button_text': button_text})


def download_excel(request):
    # 세션에서 특정 값을 확인하여 다운로드 권한이 있는지 확인
    if not request.session.get('can_download', False):
        return HttpResponse("Unauthorized access", status=403)
    
    responses = SurveyResponse.objects.all()

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append([
        '이름', 
        '직무', 
        '직급', 
        '휴대폰 번호', 
        'Email', 
        'Docker Desktop TCP 2375 포트를 사용하고 있습니까?', 
        'Docker Desktop ECI(Enhanced Container Isolation)를 사용하고 있습니까?', 
        'Docker Desktop을 WSL을 통해 사용하고 있습니까?', 
        'Docker Desktop의 engine 설정값 이미지 첨부 부탁드립니다.',
        'Docker Desktop의 Beta와 Experimental 기능들에 대한 생각을 자유롭게 말씀해주세요.',
        'Docker Desktop에서 kubernetes를 사용하고 있습니까?',
        'Docker Desktop에서 Window Container의 engine 설정값 이미지 첨부 부탁드립니다.' ,
        'Docker Desktop proxy 설정값 이미지 첨부 부탁드립니다.', 
        'Docker Desktop Extensions을 사용하고 있습니까?',
        'Docker Desktop에서 Docker scout을 사용하고 있습니까?',
        'docker load 명령어를 통해 압축된 docker image를 해제하는 경우가 많습니까?',
        'Docker Desktop update를 주기적으로 합니까?',
        'Docker Desktop의 File sharing을 사용하고 있습니까?'
    ])

    for response in responses:
        image_url_4 = response.question_4.url if response.question_4 else 'No Image'
        image_url_7 = response.question_7.url if response.question_7 else 'No Image'
        image_url_8 = response.question_8.url if response.question_8 else 'No Image'
        ws.append([
            response.name, 
            response.position, 
            response.title, 
            response.phone_number, 
            response.email, 
            response.question_1, 
            response.question_2, 
            response.question_3,
            image_url_4,
            response.question_5,
            response.question_6,
            image_url_7,
            image_url_8,
            response.question_9,
            response.question_10,
            response.question_11,
            response.question_12,
            response.question_13      
        ])

    # 현재 날짜를 가져와서 파일 이름에 포함
    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f"survey_responses_{current_date}.xlsx"
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={filename}'
    wb.save(response)
    return response




def create_admin_user(request):
    # AdminUser가 이미 존재하는지 확인
    if AdminUser.objects.exists():
        return redirect('/survey/result/')  # 이미 존재하면 로그인 페이지로 리디렉션
    
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/survey/result/')  # Admin 계정 생성 후 로그인 페이지로 리디렉션
    else:
        form = AdminUserCreationForm()

    return render(request, 'survey/create_admin.html', {'form': form})

def result_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                admin_user = AdminUser.objects.get(username=username, password=password)
                request.session['admin_user_id'] = admin_user.id
                return redirect('/survey/result/dashboard/')
            except AdminUser.DoesNotExist:
                form.add_error(None, "Invalid credentials")
    else:
        form = AdminLoginForm()

    return render(request, 'survey/result_login.html', {'form': form})

def result_dashboard(request):
    admin_user_id = request.session.get('admin_user_id')
    if not admin_user_id:
        return redirect('/survey/result/')
    

    request.session['can_download'] = True

    return render(request, 'survey/result_dashboard.html', {})


def download_json(request):
    # 세션에서 특정 값을 확인하여 다운로드 권한이 있는지 확인
    if not request.session.get('can_download', False):
        return HttpResponse("Unauthorized access", status=403)
    
    responses = SurveyResponse.objects.all()
    
    # 응답이 없을 경우 처리
    total_responses = responses.count()
    if total_responses == 0:
        return HttpResponse("No survey responses available", status=400)
    
    # 초기 JSON 설정
    json_data = {
        "configurationFileVersion": 2
    }

    # 응답을 분석하기 위해 Counter를 사용
    counter_tcp_2375 = Counter([response.question_1 for response in responses])
    counter_eci = Counter([response.question_2 for response in responses])
    counter_wsl = Counter([response.question_3 for response in responses])
    counter_kubernetes = Counter([response.question_6 for response in responses])
    counter_extensions = Counter([response.question_9 for response in responses])
    counter_scout = Counter([response.question_10 for response in responses])
    counter_docker_load = Counter([response.question_12 for response in responses])

    # 조건별로 JSON 설정 추가
    if counter_tcp_2375['미사용'] / total_responses >= 0.9:
        json_data["exposeDockerAPIOnTCP2375"] = {
            "locked": True,
            "value": False
        }

    if counter_eci['사용'] > 0:
        json_data["enhancedContainerIsolation"] = {
            "locked": True,
            "value": True
        }

    if counter_wsl['사용'] / total_responses >= 0.9:
        json_data["linuxVM"] = {
            "wslEngineEnabled": {
                "locked": False,
                "value": False
            }
        }

    if counter_kubernetes['사용'] / total_responses >= 0.9:
        json_data["kubernetes"] = {
            "locked": True,
            "enabled": True
        }

    if counter_extensions['사용'] / total_responses >= 0.1:
        json_data["extensionsEnabled"] = {
            "locked": True,
            "value": True
        }

    if counter_scout['사용'] / total_responses >= 0.1:
        json_data["scout"] = {
            "locked": True,
            "sbomIndexing": True,
            "useBackgroundIndexing": True
        }

    if counter_docker_load['없음'] == total_responses:
        json_data["blockDockerLoad"] = {
            "locked": True,
            "value": True
        }

    # JSON 데이터를 문자열로 변환
    json_str = json.dumps(json_data, indent=4, ensure_ascii=False)

    # HTTP 응답으로 JSON 파일 생성
    response = HttpResponse(json_str, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="admin-settings.json"'
    
    return response