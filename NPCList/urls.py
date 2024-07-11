from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('writingadvice/', views.writingadvice, name='writingadvice'),
    path('NPCguests/', views.NPCguests, name='NPCguests'),
    path('create_npc/', views.create_npc, name='create_npc'),  
]




