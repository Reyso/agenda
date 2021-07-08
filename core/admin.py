from django.contrib import admin
from core.models import eventos

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo' , 'data_evento' , 'data_criacao')
    list_filter = ('usuario','data_evento',) #importante a virgula no final
admin.site.register(eventos,EventoAdmin)