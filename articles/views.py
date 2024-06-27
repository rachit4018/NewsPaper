from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Article,Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # new
# Create your views here.
from django.shortcuts import get_object_or_404

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name ='article_detail.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['title', 'body',]
    login_url = 'login'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class ArticleCommentView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'Comment_Add.html'
    fields = ['comment']
    login_url = 'login'
    success_url = reverse_lazy('article_list')
    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        form.instance.article = article
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    template_name = 'comment_edit.html'
    success_url = reverse_lazy('article_list')
    fields = ['comment']
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('article_list')
    fields = ['comment']
    login_url = 'login'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user