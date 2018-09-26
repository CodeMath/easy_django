from django.shortcuts import render,redirect
from .forms import BookmarkForm
from django.views import View


def register_url(request):

    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list/')
    else:
        form = BookmarkForm()

    return render(request, 'get_url/main.html', {"form":form})


class Generic_register_url(View):

    def get(self, request):
        form = BookmarkForm()
        return render(request, 'get_url/main.html', {"form":form})

    def post(self, request):
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('List_url')
        return render(request, 'get_url/main.html', {"form":form})

