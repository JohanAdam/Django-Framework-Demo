from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #as_view() = take this class as view

    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/<album_id>/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/<album_id>/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    #/music/album/song/add/
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),

    #/music/album/<album_id>/song
    url(r'song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song-update'),

    #/song/id/delete
    url(r'song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),
]
