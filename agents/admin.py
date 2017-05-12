from django.contrib import admin
from .models import Agent, Group
# Register your models here.

admin.site.register(Agent)

class GroupAdmin(admin.ModelAdmin):
    filter_vertical = ('members', 'linked')

admin.site.register(Group, GroupAdmin)

