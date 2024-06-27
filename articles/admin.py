from django.contrib import admin
from .models import Article,Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class Articleadmin(admin.ModelAdmin):
    inlines =[
        CommentInline,
    ]

admin.site.register(Article,Articleadmin)
admin.site.register(Comment)