from django.urls import reverse_lazy,path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleCommentView,
    CommentEditView,
    CommentDeleteView,
)

urlpatterns =[
    path('', ArticleListView.as_view(),name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(),name='article_detail'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(),name='article_edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(),name='article_delete'),
    path('new/',ArticleCreateView.as_view(),name='article_create'),
    path('comment/<int:pk>/', ArticleCommentView.as_view(), name='article_comment'),
    path('comment/edit/<int:pk>/', CommentEditView.as_view(), name='comment_edit'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),



]