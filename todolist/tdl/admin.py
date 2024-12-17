from django.contrib import admin
from .models import Tasks, History

# Register your models here.
@admin.register(Tasks)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','task','description']
    list_display_links = ['task']

@admin.register(History)
class AdminHistory(admin.ModelAdmin):
    list_display = ['id','htask','hdescription']
    list_display_links = ['htask']