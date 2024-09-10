from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Members
from .forms import MemberForm

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.

class MembersListView(ListView):

    model = Members
    
    template_name = "game/members/list.html"
    
    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            membersList = Members.objects.filter(
                name__icontains=query)
        else:
            membersList = Members.objects.all()
        
        return membersList
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "修練生一覧"
        context["query"] = self.request.GET.get("query")  # クエリをコンテキストに追加
        return context

class MembersCreateView(CreateView):
    
    model = Members
    
    form_class = MemberForm
    
    required=True
    
    success_url = reverse_lazy("game:MembersListView")
    
    template_name = "game/members/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "修練生新規作成"
        context["message"] = "フォームを入力してください"
        return context

class MembersDetailView(DetailView):
    model = Members
    template_name = "game/members/detail.html"
    context_object_name = "member"  # モデルインスタンスにアクセスするための名前
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "修練生詳細"
        return context
        

class MemberUpdateView(UpdateView):
    model = Members
    
    form_class = MemberForm
    
    success_url = reverse_lazy("game:MembersListView")
    
    template_name = "game/members/update.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "修練生の情報更新"
        context["message"] = "修練生の情報を更新します"
        return context
        
        
class MemberDeleteView(DeleteView):
    model = Members
    
    success_url = reverse_lazy("game:MembersListView")
    
    def get(self, *args ,**kwargs):
        pk = self.kwargs.get("pk")
        object = Members.objects.get(id=pk)
        object.delete()
        return redirect(self.success_url)
    