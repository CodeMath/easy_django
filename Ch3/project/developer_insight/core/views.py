from django.shortcuts import redirect, get_object_or_404
from board.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="account_session")
def reply(request,id):
    if request.method == "POST":
        comment = request.POST.get('comment')
        board = get_object_or_404(Board, id=id)
        Reply.objects.create(
            user=request.user,
            content=comment,
            article_id = id,
            ip=get_ipaddress(request)
        )
    return redirect('Article_View', id=board.table, pk=board.id)

@login_required(login_url="account_session")
def article_vote(request,id,vote_type):
    board = get_object_or_404(Board,id=id)
    if request.user not in board.up_vote_user.all() and request.user not in board.down_vote_user.all():
        if vote_type == "up":
            board.up_vote_user.add(request.user)
            board.up_vote += 1
        elif vote_type == "down":
            board.down_vote_user.add(request.user)
            board.down_vote += 1
        board.save()

    return redirect('Article_View', id=board.table, pk=board.id)


def get_ipaddress(request):
    """Return ipaddress"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


