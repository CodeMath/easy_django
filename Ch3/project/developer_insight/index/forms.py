from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = {"username","first_name", "password1","password2"}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = "form-control required"
        self.fields['first_name'].widget.attrs["class"] = "form-control required"
        self.fields['password1'].widget.attrs["class"] = "form-control required"
        self.fields['password2'].widget.attrs["class"] = "form-control required"

        self.fields['username'].widget.attrs["placeholder"] = "이메일을 입력하세요."
        self.fields['first_name'].widget.attrs["placeholder"] = "닉네임"
        self.fields['password1'].widget.attrs["placeholder"] = "비밀번호"
        self.fields['password2'].widget.attrs["placeholder"] = "비밀번호 확인"
