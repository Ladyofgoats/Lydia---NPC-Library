#from django.urls import path
#from . import views

#urlpatterns = [
    #url('admin/',admin.site.urls),
    #url(r'^about/$',views.about),
    #url(r'^$',views.homepage)
#]
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/',admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', include('NPCList.urls')), 
    path("", include("NPCList.urls"), name="NPCList-urls"),
]
