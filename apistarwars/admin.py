from django.contrib import admin
from apistarwars.models import peliculas, planeta, Personaje
# Register your models here.
class peliculasAdmin(admin.ModelAdmin):
    list_display=("nombre","texto_apertura","director","productores")
    
    list_filter=("personajes","planetas",)

class personajesAdmin(admin.ModelAdmin):
    list_display=("id","nombre")

class planetasAdmin(admin.ModelAdmin):
    list_display=("id","nombre")

admin.site.register(peliculas, peliculasAdmin)
admin.site.register(Personaje,personajesAdmin)
admin.site.register(planeta,planetasAdmin)
