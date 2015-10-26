from django.contrib import admin

from .models import Board, Thread, Comment


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'link',
        'body',
        'board',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = [
        'body',
        'thread',
        'parent',
    ]