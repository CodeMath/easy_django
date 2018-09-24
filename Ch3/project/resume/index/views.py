from django.shortcuts import render
from .models import MyProfile, MyInformation

# Create your views here.
def main(request):
    profile = MyProfile.objects.get(id=1)
    project = MyInformation.objects.filter(types__types="프로젝트")
    intern = MyInformation.objects.filter(types__types="인턴")
    return render(request, 'index/main.html', {"profile":profile, "project":project, "intern":intern})