#from django.contrib import admin
#from django.urls import path
#from . import views

#urlpatterns = [
    #url('admin/',admin.site.urls),
    #url(r'^about/$',views.about),
    #url(r'^$',views.homepage)
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('writingadvice/', views.writingadvice, name='writingadvice'),
     path('NPCList/', views.NPCList, name='NPClist'),
]
