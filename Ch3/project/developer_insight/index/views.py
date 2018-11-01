from django.shortcuts import render, redirect
from board.models import *
from django.contrib.auth.models import User
from board.table import BoardConfig
from .forms import *
from django.contrib.auth import login, authenticate

from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy

from django.contrib.syndication.views import Feed

# Create your views here.
def index(request):
    board = Board.objects.all().exclude(status="deleted").order_by('-id')[:6]
    user = User.objects.all().order_by('-id')[:3]
    board_table = BoardConfig.BOARD_TABLE
    data={
        "board":board,
        "user":user,
        "board_table":board_table,
        "active":"index"
    }
    return render(request,'index/index.html',data)


def account_session(request):
    msg = ""
    if request.method == "POST":
        check = request.POST.get("type")
        # 회원가입
        if check == "signup":
            signupform = SignUpForm(request.POST)
            if signupform.is_valid():
                signupform.save()
                return redirect('index')
            else:
                msg = signupform.errors

        # 로그인
        else:
            id = request.POST.get("username")
            pw = request.POST.get("password")

            user = authenticate(username = id, password = pw)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                msg = "아이디/비밀번호를 확인해주세요."

            signupform = SignUpForm()

    else:
        signupform = SignUpForm()

    board_table = BoardConfig.BOARD_TABLE
    data={
        "signupform":signupform,
        "msg":msg,
        "board_table":board_table
    }
    return render(request,'account/account.html', data)


class DDC_Feed(Feed):
    title="Django Developer Community"
    link = "/board/"
    description = "Django Developer Community - Recent 10"

    def items(self):
        return Board.objects.filter(status="normal").order_by("-id")[:10]

    def item_title(self,item):
        return item.title

    def item_link(self, item):
        return reverse_lazy('Article_View', kwargs={"id":item.table, "pk":item.pk})


class DDC_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Board.objects.filter(status="normal")

    def location(self, obj):
        return reverse_lazy('Article_View', kwargs={"id":obj.table, "pk":obj.pk})

    def lastmod(self, obj):
        return obj.created

class Static_URL(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['index','account_session']

    def location(self, obj):
        return reverse_lazy(obj)