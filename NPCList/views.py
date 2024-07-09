from django.shortcuts import render, redirect
from .models import NPC
from .forms import NPCentries

# Create your views here.
#def npc_entries(request):
    #return render(request, 'app-templates/npc-entries.html')

def homepage(request):
    " home_page view"
    return render(request,'index.html')


def about(request):
    " about view"
    return render(request,'about.html')

def writingadvice(request):
    " writingadvice view"
    return render(request, 'writingadvice.html')




# def NPCentries(request):
#     if request.method == 'POST':
#         form = NPCentries(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog:entry_list')  # Replace 'entry_list' with your actual URL name for listing entries
#     else:
#         form = NPCentries()
#     return render(request, 'template/NPCentries.html', {'form': form})
