from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import NPC
from .forms import NPCentries

# Create your views here.

@login_required
def homepage(request):
    """Home page view"""
    return render(request, 'NPCList/homepage.html')  # Ensure this template exists

@login_required
def about(request):
    """About view"""
    return render(request, 'NPCList/about.html')

@login_required
def writing_advice(request):
    """Writing advice view"""
    return render(request, 'NPCList/writing_advice.html')

@login_required
def NPCguests(request):
    """NPC guests view"""
    return render(request, 'NPCList/NPCguests.html')






# def NPCentries(request):
#     if request.method == 'POST':
#         form = NPCentries(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:entry_list')  # Replace 'entry_list' with your actual URL name for listing entries
#     else:
#         form = NPCentries()
#     return render(request, 'template/NPCentries.html', {'form': form})
