from django.contrib import admin

from django.contrib import admin
from .models import Veiculo

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'cor', 'combustivel', 'foto']
    search_fields = ['modelo']
    
admin.site.register(Veiculo, VeiculoAdmin)
# Register your models here.
