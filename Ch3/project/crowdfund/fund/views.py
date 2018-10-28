from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from index.models import MyFunding

def view_funding(request, id):
    funding = get_object_or_404(Funding, pk=id)
    news = Funding_News.objects.filter(is_funding=funding)
    msg = ""
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('signin')
        reward_id = request.POST.get('reward')
        is_reward = get_object_or_404(Reward, pk=reward_id)
        if is_reward.number == 0:
            msg = "해당 리워드는 마감되었습니다."
        else:
            if is_reward.number > 0:
                is_reward.number -= 1
                is_reward.save()
            funding.now_funding += is_reward.price
            funding.save()

            MyFunding.objects.create(
                user=request.user,
                is_funding=funding,
                reward=is_reward
            )
            return redirect('mypage')

    return render(request, 'fund/funding.html', {"funding":funding,"news":news, "msg":msg})

@login_required(login_url='signin')
def register(request):
    if not request.user.is_staff:
        return redirect('index')

    if request.method == "POST":
        forms = FundingForm(request.POST, request.FILES)
        r_forms = RewardForm(request.POST)

        if forms.is_valid():
            # 작성자 저장하기 위한, 데이터베이스 미등록 상태
            registed = forms.save(commit=False)
            registed.writer = request.user
            registed.save()

            # reward
            if r_forms.is_valid():
                basic_reward = r_forms.save()

                # 리워드 추가하기
                registed.reward.add(
                    basic_reward
                )
                registed.save()


                return redirect('index')
            else:
                msg = r_forms.errors
        else:
            msg = forms.errors
    else:
        forms = FundingForm()
        r_forms = RewardForm()
        msg = ""

    return render(request, 'fund/register.html',
                  {"forms":forms,"r_forms":r_forms, "msg":msg})


@login_required(login_url='signin')
def funding_news(request, id):
    # 펀딩 소식 업데이트를 위한 펀딩 조회 & 게시자 검증
    is_funding = get_object_or_404(Funding, pk=id)
    if is_funding.writer != request.user:
        return redirect('index')
    msg = ""
    if request.method == "POST":
        forms = FundingNewsForm(request.POST)
        if forms.is_valid():
            news = forms.save(commit=False)
            news.is_funding=is_funding
            news.save()
            msg = "업데이트 완료"
        else:
            msg = forms.errors

    forms = FundingNewsForm()
    return render(request, 'fund/edit_funding.html', {"forms":forms, "msg":msg})

@login_required(login_url='signin')
def add_reward(request, id):
    is_funding = get_object_or_404(Funding, pk=id)
    if is_funding.writer != request.user:
        return redirect('index')

    msg = ""

    if request.method == "POST":
        forms = RewardForm(request.POST)
        if forms.is_valid():
            reward = forms.save()

            is_funding.reward.add(
                reward
            )
            is_funding.save()

            msg = "등록완료"

        else:
            msg = forms.errors

    forms = RewardForm()

    return render(request, 'fund/edit_funding.html', {"forms":forms, "msg":msg})