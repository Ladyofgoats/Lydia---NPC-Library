from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import NPC
from django.views import generic
from .forms import NPCentries

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
    entries = NPC.objects.all().order_by('date')
    return render(request, 'NPCList/NPCguests.html', {'entries': entries})

@login_required
def create_npc(request):
    """Create NPC view"""
    if request.method == 'POST':
        form = NPCentries(request.POST)
        if form.is_valid():
            npc = form.save(commit=False)
            npc.author = request.user
            npc.save()
            return redirect('NPCguests')  
    else:
        form = NPCentries()
    return render(request, 'NPCList/add_npc.html', {'form': form})

@login_required
def edit_npc(request, slug):
    npc = NPC.objects.get(slug=slug)
    if request.method == 'POST':
        form = NPCentries(request.POST, instance=npc)
        if form.is_valid():
            form.save()
            return redirect('NPCguests')
    else:
        form = NPCentries(instance=npc)
    return render(request, 'NPCList/edit_npc.html', {'form': form})

@login_required
def delete_npc(request, slug):
    npc = NPC.objects.get(slug=slug)
    if request.method == 'POST':
        npc.delete()
    return redirect('NPCguests')

@login_required
def show_npc(request, slug):
    """Show NPC view"""
    entry = NPC.objects.get(slug=slug)
    return render(request, 'NPCList/show_npc.html', {'entry': entry})
    











