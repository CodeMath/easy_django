from django.shortcuts import render
from .models import History
from django.http import JsonResponse

def index(request):
    s = request.GET.get('s', "이더리움")
    data = History.objects.filter(name=s)
    return render(request, 'index/index.html',{"data":data})


def get_data(request):

    asks=request.GET.get('asks')
    bids=request.GET.get('bids')
    name=request.GET.get('name')

    History.objects.create(
        name=name,
        asks=asks.split(" ")[2],
        bids=bids.split(" ")[2],
        asks_vol=asks.split(" ")[3],
        bids_vol=bids.split(" ")[3]
    )

    return JsonResponse({"ok":True})