from django.views.generic.list import ListView
from get_url.models import Bookmark

class List_url(ListView):

    template_name = "list_url/list.html"
    model = Bookmark
    paginate_by = 5

class Search_ListView(ListView):
    template_name = "list_url/list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Bookmark.objects.all()
        if self.request.GET.get("q"):
            tag = self.request.GET.get("q")
            queryset = Bookmark.objects.filter(tag__text=tag)
        return queryset
