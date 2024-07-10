from django.contrib import admin
from .models import NPC

@admin.register(NPC)
class NPCAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'genre', 'job', 'date', 'author')
    prepopulated_fields = {'slug': ('name',)}

# If you have other models like Task, register them similarly
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'npc', 'status', 'due_date')

