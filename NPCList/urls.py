from django.urls import path
from . import views

# app_name = 'NPCList'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('writing_advice/', views.writing_advice, name='writing_advice'),
    path('NPCguests/', views.NPCguests, name='NPCguests'),
    # path('writingadvice/', views.writingadvice, name='writingadvice'),   
]