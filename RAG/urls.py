from django.urls import path
from . import views

app_name = 'RAG'

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
] 