from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import NPC
from .forms import NPCentries
from django.views import generic


# Create your views here.


class PostList(generic.ListView):
    model = NPC

@login_required
def homepage(request):
    """Home page view"""
    return render(request, 'NPCList/homepage.html')  # Ensure this template exists

@login_required
def about(request):
    """About view"""
    return render(request, 'NPCList/about.html')

@login_required
def writingadvice(request):
    """Writing advice view"""
    return render(request, 'NPCList/writingadvice.html')

@login_required
def NPCguests(request):
    """NPC guests view"""
    return render(request, 'NPCList/NPCguests.html')



def NPCentries(request):
    entries = NPC.object.all.order_by('date')
    return render(request, 'entires/NPCguests.html', {'entries':entries})