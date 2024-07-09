#from django.http import HttpResponse

#def homepage(request):
    #return HttpResponse('homepage')

#def about(request):
    #return HttpResponse('about')

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("This is the homepage")
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse("This is the about page.")
    return render(request, 'about.html')

def writingadvice(request):
    #return HttpResponse("This is the Writing advice page.")
    return render(request, 'writingadvice.html')

def NPCguests(request):
    #return HttpResponse("This is the Writing advice page.")
    return render(request, 'NPCguests.html')