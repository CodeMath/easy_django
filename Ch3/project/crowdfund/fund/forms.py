from django import forms
from .models import Funding, Reward, Funding_News
from django_summernote.widgets import SummernoteWidget

class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding

        fields = (
            'title','content','main_img','to_finish','funding_goal'
        )
        # exclude = (
        #     'writer','finish','reward','now_funding'
        # )
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(FundingForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs["class"] = "form-control required"
        self.fields['main_img'].widget.attrs["class"] = "form-control required"
        self.fields['to_finish'].widget.attrs["class"] = "form-control required"
        self.fields['funding_goal'].widget.attrs["class"] = "form-control required"


class RewardForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RewardForm, self).__init__(*args, **kwargs)

        self.fields['subject'].widget.attrs["class"] = "form-control required"
        self.fields['content'].widget.attrs["class"] = "form-control required"
        self.fields['price'].widget.attrs["class"] = "form-control required"
        self.fields['number'].widget.attrs["class"] = "form-control required"

class FundingNewsForm(forms.ModelForm):
    class Meta:
        model=Funding_News
        exclude=(
            'is_funding',
        )

    def __init__(self, *args, **kwargs):
        super(FundingNewsForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs["class"] = "form-control required"
        self.fields['content'].widget.attrs["class"] = "form-control required"

