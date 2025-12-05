from django.contrib import admin
from works.models import *



class TaskInline(admin.TabularInline):
    model = Task
    extra = 0


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline
    ]
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = [
        "numbers",
    ]