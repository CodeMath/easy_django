from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = {"username", "password1","password2"}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = "form-control required"
        self.fields['password1'].widget.attrs["class"] = "form-control required"
        self.fields['password2'].widget.attrs["class"] = "form-control required"
