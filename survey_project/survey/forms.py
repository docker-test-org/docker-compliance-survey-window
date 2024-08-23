from django import forms
from .models import SurveyResponse

class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['name', 'position', 'title', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'position': forms.TextInput(attrs={'autocomplete': 'off'}),
            'title': forms.TextInput(attrs={'autocomplete': 'off'}),
            'phone_number': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
        }

class SurveyQuestionsForm(forms.ModelForm):
    CHOICES = [
        ('사용', '사용'),
        ('미사용', '미사용')
    ]

    CHOICES2 = [
        ('아주 많음', '아주 많음'),
        ('많음', '많음'),
        ('보통', '보통'),
        ('거의 없음', '거의 없음'),
        ('없음','없음')
    ]

    CHOICES3 = [
        ('3~4개월 주기', '3~4개월 주기'),
        ('5~6개월 주기', '5~6개월 주기'),
        ('1년 주기', '1년 주기'),
        ('업데이트 하지 않음', '업데이트 하지 않음'),
    ]


    # 객관식 질문 (라디오 버튼)
    question_1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Docker Desktop TCP 2375 포트를 사용하고 있습니까?")

    # 객관식 질문 (라디오 버튼)
    question_2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Docker Desktop ECI(Enhanced Container Isolation)를 사용하고 있습니까?")

    # 객관식 질문 (라디오 버튼)
    question_3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Docker Desktop을 WSL을 통해 사용하고 있습니까?")

    # 사진 첨부 (선택사항)
    question_4 = forms.ImageField(required=False, label="Docker Desktop의 engine 설정값 이미지 첨부 부탁드립니다. (선택사항)")

    # 주관식 질문 (텍스트 입력)
    question_5 = forms.CharField(widget=forms.Textarea, label="Docker Desktop의 Beta와 Experimental 기능들에 대한 생각을 자유롭게 말씀해주세요.")

    # 객관식 질문 (라디오 버튼)
    question_6 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Docker Desktop에서 kubernetes를 사용하고 있습니까?")

    # 사진 첨부 (선택사항)
    question_7 = forms.ImageField(required=False, label="Docker Desktop에서 Window Container의 engine 설정값 이미지 첨부 부탁드립니다. (선택사항)")

    # 사진 첨부 (선택사항)
    question_8 = forms.ImageField(required=False, label="Docker Desktop proxy 설정값 이미지 첨부 부탁드립니다. (선택사항)")

    # 객관식 질문 (라디오 버튼)
    question_9 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Docker Desktop Extensions을 사용하고 있습니까?")

    # 객관식 질문 (라디오 버튼)
    question_10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Docker Desktop에서 Docker scout을 사용하고 있습니까?")

    # 객관식 질문 (라디오 버튼)
    question_11 = forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect, label="docker load 명령어를 통해 압축된 docker image를 해제하는 경우가 많습니까?")

    # 객관식 질문 (라디오 버튼)
    question_12 = forms.ChoiceField(choices=CHOICES3, widget=forms.RadioSelect, label="Docker Desktop update를 주기적으로 합니까?")

    # 객관식 질문 (라디오 버튼)
    question_13 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Docker Desktop의 File sharing을 사용하고 있습니까?")

    class Meta:
        model = SurveyResponse
        fields = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7' , 'question_8', 'question_9', 'question_10', 'question_11', 'question_12', 'question_13' ]



from django import forms
from .models import AdminUser

class AdminUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AdminUser
        fields = ['username', 'password']

    def save(self, commit=True):
        admin_user = super().save(commit=False)
        if commit:
            admin_user.save()
        return admin_user


class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
