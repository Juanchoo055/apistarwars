from django.urls import path
from apistarwars import views




urlpatterns = [
    path('', views.home, name='Home'),

    #path para CRUD de personajes
    path('api/personajes/',views.personajesview.as_view(), name='personajes_list' ),
    path('api/personajes/<int:id>',views.personajesview.as_view(), name='personajes_process' ),
    path('api/personajes/add/',views.personajesviewadd.as_view(), name='personajes_add' ),

    #path para CRUD de peliculas
    path('api/peliculas/',views.peliculasview.as_view(), name='peliculas_list'),
    path('api/peliculas/<int:id>',views.peliculasview.as_view(), name='peliculas_process' ),
    path('api/peliculas/add/',views.peliculasviewadd.as_view(), name='peliculas_add' ),

        #path para CRUD de planetas
    path('api/planetas/',views.planetasview.as_view(), name='planetas_list'),
    path('api/planetas/<int:id>',views.planetasview.as_view(), name='planetas_process' ),
    path('api/planetas/add/',views.planetasviewadd.as_view(), name='planetas_add' ),
]