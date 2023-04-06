from django.shortcuts import render
from django.views.generic import *
from Peliculeando.models import *
from django.urls import *

# Create your views here.

def index(request):
    return render(request, "Peliculeando/index.html")

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post-list')

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post-list')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
