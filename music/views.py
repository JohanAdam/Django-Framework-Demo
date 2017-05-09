#separated html from python
from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.
#request is html request
def index(request):
    all_albumpara = Album.objects.all()
    return render(request, 'music/index.html', {'all_albumss': all_albumpara})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
