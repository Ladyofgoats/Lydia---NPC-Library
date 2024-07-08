from django.contrib import admin
#from django.urls import path
#from . import views

#urlpatterns = [
    #url('admin/',admin.site.urls),
    #url(r'^about/$',views.about),
    #url(r'^$',views.homepage)
#]

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('NPCList.urls')),  
]
