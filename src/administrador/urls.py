from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "administrador"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', views.registro, name = "registrarse"),

    path('login/', views.logeo, name = "logearse"),
]
