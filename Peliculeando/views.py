from django.shortcuts import render
from django.views.generic import *
from Peliculeando.models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import *

# Create your views here.

def index(request):
    return render(request, "Peliculeando/index.html")

class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Post
    fields = ['nombre_pelicula','año_estreno','reseña_pelicula','valoracion_final','imagen']
    success_url = reverse_lazy('post-list')
    
    def form_valid(self, form):
        form.instance.autorizado = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return hasattr(self.request.user, 'profile')

    def handle_no_permission(self):
        return render(self.request, "Peliculeando/not_profile.html")


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['nombre_pelicula','año_estreno','reseña_pelicula','valoracion_final','imagen']
    success_url = reverse_lazy('post-list')

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(autorizado=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Peliculeando/not_found.html")

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Post.objects.filter(autorizado=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Peliculeando/not_found.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')
    
class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):
    template_name = "registration/logout.html"

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['genero_preferido','imagen','pelicula_preferida']
    success_url = reverse_lazy('post-list')

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Peliculeando/not_found.html")

class ProfileDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('post-list')

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Peliculeando/not_found.html")

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['genero_preferido','imagen','pelicula_preferida']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileDetail(DetailView):
    model = Profile