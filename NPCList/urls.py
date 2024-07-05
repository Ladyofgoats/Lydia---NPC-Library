from django.urls import path
from . import views

urlpatterns = [
    path('', views.NPC_Entries, name='NPC_Entries'),
]