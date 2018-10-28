from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from fund.models import *
from .models import MyFunding

# Create your views here.
def index(request):

    funding = Funding.objects.exclude(finish=True)

    return render(request, 'index/index.html', {"funding":funding})


def signup(request):
    if request.method == "POST":
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
        else:
            msg = forms.errors
    else:
        msg= ""
        forms = SignUpForm()

    return render(request, 'index/signup.html', {"signup": forms, 'msg': msg})

@login_required(login_url='signin')
def mypage(request):
    if request.user.is_staff:
        my_funding = Funding.objects.filter(writer=request.user)
    else:
        my_funding = []
    fundings = MyFunding.objects.filter(user=request.user)

    return render(request,'index/mypage.html', {"my_funding":my_funding, "fundings":fundings})