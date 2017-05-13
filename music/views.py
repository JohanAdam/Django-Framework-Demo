# separated html from python
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
#this module will take user name and password to verify if he a user
#in the database.
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


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

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    #before submit
    def get(self, request):

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #when press submit ; post the data
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        print("post method.")

        if form.is_valid():
            print("form is valid.")

            user = form.save(commit=False)
            #not save in databse yet ; save in parameter
            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            #save in database
            user.save()

            email = self.cleaned_data.get('email')
            if email:
                if User.objects.filter(email=email).exists():
                    raise forms.ValidationError('Your email is not unique.')

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                print("user is not none.")

                if user.is_active:
                    print('user active')
                    #not banned
                    login(request, user)
                    return redirect('music:index')

        #false goes here
        print('return')
        return render(request, self.template_name, {'form': form})
