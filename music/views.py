#separated html from python
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.
#request is html request
def index(request):
    all_albumpara = Album.objects.all()
    return render(request, 'music/index.html', {'all_albumss': all_albumpara})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        #try get something
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        #can't get it
        return render(request, 'music/detail.html', {
            'album':album,
            'error_message':"You did not select a valid sond",
        })
    else:
        #after get try get everything it wants
        if selected_song.is_favourite:
            selected_song.is_favourite = False
        else:
            selected_song.is_favourite = True

        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})





