from django.shortcuts import render,get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from board.table import BoardConfig

@login_required(login_url='account_session')
def SendMessage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        messages = request.POST.get('comment')

        user = get_object_or_404(User,first_name=username)

        Message.objects.create(
            sender=request.user,
            receiver=user,
            content=messages
        )
    board_table = BoardConfig.BOARD_TABLE
    message = Message.objects.filter(Q(sender=request.user)|Q(receiver=request.user)).order_by('-created')
    data={
        "board_table":board_table,
        "message":message,
        'u':request.GET.get('u','')
    }
    return render(request, 'send/send.html',data)