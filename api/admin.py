from django.contrib import admin
from .models import Survivor

class SurvivorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex', 'infected', 'points', 'reports')
    list_filter = ('infected',)
    search_fields = ('name', 'age', 'sex', 'points', 'reports')

admin.site.register(Survivor, SurvivorAdmin)
