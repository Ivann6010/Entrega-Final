"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Peliculeando.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    #about
    path('about/', about, name="about"),
    # index
    path('', index, name="index"),
    # registro user
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    # post crud
    path('post/list', PostList.as_view(), name="post-list"),
    path('post/create', PostCreate.as_view(), name="post-create"),
    path('post/detail/<pk>', PostDetail.as_view(), name="post-detail"),
    path('post/update/<pk>', PostUpdate.as_view(), name="post-update"),
    path('post/delete/<pk>', PostDelete.as_view(), name="post-delete"),
    # profile crud
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('profile/update/<pk>', ProfileUpdate.as_view(), name="profile-update"),
    path('profile/detail/<pk>', ProfileDetail.as_view(), name="profile-detail"),
    path('profile/delete/<pk>', ProfileDelete.as_view(), name="profile-delete"),
    # mensajes
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/delete/<pk>', MensajeDelete.as_view(), name="mensaje-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)