from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from .models import Board, Thread, Comment
from .forms import ThreadForm, CommentForm


class Home(View):

    def get(self, request, *args, **kwargs):
        page_title = 'Home'
        context = {
            'page_title': page_title,
        }
        return render(
            request,
            'forums/home.html',
            context
        )


class BoardList(View):

    def get(self, request, *args, **kwargs):
        boards = Board.objects.all()
        page_title = 'Board List'
        context ={
            'page_title': page_title,
            'boards': boards,
        }
        return render(
            request,
            'forums/board_list.html',
            context
        )


class BoardView(View):

    def get(self, request, *args, **kwargs):
        board = get_object_or_404(Board, slug=kwargs['board_slug'])
        threads = Thread.objects.filter(board=board)
        thread_form = ThreadForm()
        page_title = board.name
        context = {
            'page_title': page_title,
            'board': board,
            'threads': threads,
            'thread_form': thread_form,
        }
        return render(
            request,
            'forums/board.html',
            context
        )

    def post(self, request, *args, **kwargs):
        board = get_object_or_404(Board, slug=kwargs['board_slug'])
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            new_thread = thread_form.save(commit=False)
            new_thread.board = board
            new_thread.save()
            return HttpResponseRedirect(
                reverse(
                    'forums:thread_view',
                    kwargs={
                        'board_slug': board.slug,
                        'thread_id': new_thread.id,
                    },
                )
            )
        return HttpResponseRedirect('#')


class ThreadView(View):

    def get(self, request, *args, **kwargs):
        board = get_object_or_404(Board, slug=kwargs['board_slug'])
        thread = get_object_or_404(Thread, id=kwargs['thread_id'])
        comments = Comment.objects.filter(thread=thread)
        comment_form = CommentForm()
        page_title = thread.title
        context = {
            'page_title': page_title,
            'board': board,
            'thread': thread,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(
            request,
            'forums/thread.html',
            context
        )

    def post(self, request, *args, **kwargs):
        thread = get_object_or_404(Thread, id=kwargs['thread_id'])
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if 'parent_comment_id' in request.POST:
                parent_comment = Comment.objects.get(
                    id=comment_form.data['parent_comment_id']
                )
                new_comment = comment_form.save(commit=False)
                new_comment.parent = parent_comment
                new_comment.thread = thread
                new_comment.save()
            new_comment = comment_form.save(commit=False)
            new_comment.thread = thread
            new_comment.save()
            return HttpResponseRedirect('#')


class MetaView(View):

    def get(self, request, *args, **kwargs):
        page_title = 'Meta'
        context = {
            'page_title': page_title,
        }
        return render(
            request,
            'forums/meta.html',
            context
        )


class AboutView(View):

    def get(self, request, *args, **kwargs):
        page_title = 'About'
        context ={
            'page_title': page_title,
        }
        return render(
            request,
            'forums/about.html',
            context
        )
