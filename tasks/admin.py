from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)

admin.site.register(Task, TaskAdmin)

