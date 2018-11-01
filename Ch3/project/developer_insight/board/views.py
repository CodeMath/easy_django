from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .table import BoardConfig
from .forms import *
from core.views import *

class Board_View(ListView):
    model = Board
    template_name = "board/board.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        # url parameter : <int:id>
        try:
            self.object_list = self.object_list.filter(
                table = kwargs["id"]
            ).exclude(status="deleted")

            context = self.get_context_data()

            context["active"] = kwargs["id"]
        except:
            self.object_list = self.object_list.exclude(status="deleted")
            context = self.get_context_data()
            context["active"] = "index"

        context["board_table"] = BoardConfig.BOARD_TABLE
        return self.render_to_response(context)


class Article_View(DetailView):
    model = Board
    template_name = "board/article.html"

    def get_context_data(self, **kwargs):

        if kwargs["object"].status != "normal":
            raise Http404()

        context = super().get_context_data(**kwargs)
        context["board_table"] = BoardConfig.BOARD_TABLE
        # kwargs = {'object':<Board:TEST>}
        context["active"] = kwargs["object"].table
        context["replys"] = Reply.objects.filter(article_id=self.object.id)
        return context

class Create_Article_View(CreateView):
    template_name = 'board/write.html'
    form_class = BoardForm

    def get(self, request, *args, **kwargs):
        context={}
        context["board_table"] = BoardConfig.BOARD_TABLE
        context["active"] = self.kwargs["id"]
        context["form"]=BoardForm
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = "normal"
        self.object.table = self.kwargs["id"]
        self.object.user = self.request.user
        self.object.ip = get_ipaddress(self.request)
        self.object.save()
        return redirect('index')

class Update_Article_View(UpdateView):
    model = Board
    template_name = 'board/write.html'
    form_class = BoardForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            raise Http404
        return super(Update_Article_View, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('index')