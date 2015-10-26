from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.Home.as_view(),
        name='home',
    ),
    url(
        r'^boards/$',
        views.BoardList.as_view(),
        name='board_list',
    ),
    url(
        r'^board/(?P<board_slug>[\W\w]+)/thread/(?P<thread_id>[\d]+)/$',
        views.ThreadView.as_view(),
        name='thread_view',
    ),
    url(
        r'^board/(?P<board_slug>[\W\w]+)/$',
        views.BoardView.as_view(),
        name='board_view',
    ),
    url(
        r'^meta/$',
        views.MetaView.as_view(),
        name='meta_view',
    ),
    url(
        r'^about/$',
        views.AboutView.as_view(),
        name='about_view',
    ),
]