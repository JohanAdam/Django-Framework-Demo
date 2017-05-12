# separated html from python
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album, Song


# List generic view
class IndexView(generic.ListView):
    # get the view
    template_name = 'music/index.html'
    # give parameter to list return
    context_object_name = "all_albums"

    # the data this view need
    def get_queryset(self):
        return Album.objects.all()
        # by default it return as object_list to the layout


# List generic view
class DetailView(generic.DetailView):
    model = Album
    # get the view
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album

    #After delete, redirect user to index.html
    success_url = reverse_lazy('music:index')

class SongCreate(CreateView):
    model = Song
    fields = ['album','song_title','file_type','is_favourite']

    # success_url = reverse_lazy('')

class SongUpdate(UpdateView):
    model = Song
    fields = ['album','song_title','file_type','is_favourite']

class SongDelete(DeleteView):
    model = Song

    #After delete, redirect user to detail
    success_url = reverse_lazy('music:index')