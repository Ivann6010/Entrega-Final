from django.shortcuts import render
from django.views.generic import *
from Peliculeando.models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    return render(request, "Peliculeando/index.html")

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post-list')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post-list')

class PostDelete(LoginRequiredMixin ,DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('post-list')
    
class Login(LoginView):
    next_page = reverse_lazy("post-list")

class Logout(LogoutView):
    template_name = "registration/logout.html"