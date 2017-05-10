# separated html from python
from django.views import generic
from .models import Album


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
