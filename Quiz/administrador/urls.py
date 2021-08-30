from django.contrib import admin
from django.urls import path, include
from .views import listar_preguntas

urlpatterns = [
    path('admin/', admin.site.urls),

    
]
