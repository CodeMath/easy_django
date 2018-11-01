from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import *

class BoardForm(forms.ModelForm):


    class Meta:
        model = Board
        fields=(
            'title','content'
        )
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': '제목을 입력하세요.', 'class': 'form-control'}
            ),
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        """Init"""
        super(BoardForm, self).__init__(*args, **kwargs)
