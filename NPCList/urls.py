from django.urls import path
from . import views

# app_name = 'NPCList'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('writing-advice/', views.writingadvice, name='writingadvice'),
    # path('writingadvice/', views.writingadvice, name='writingadvice'),   
]