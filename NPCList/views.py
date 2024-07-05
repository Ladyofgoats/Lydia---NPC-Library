from django.shortcuts import render

# Create your views here.
def npc_entries(request):
    return render(request, 'app-templates/npc-entries.html')
