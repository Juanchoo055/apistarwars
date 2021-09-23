from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Personaje, peliculas, planeta
import json

# Create your views here.

def home(request):
    return render(request,'apistarwars/inicio.html')


#VISTAS PARA PERSONAJES

class personajesview(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):

        if id > 0:
            personajes= list(Personaje.objects.filter(id=id).values())
            if len(personajes)>0:
                person = personajes[0]
                datos={'messaje':"Success", 'personajes':person}
            else:
                datos={'messaje':"Personaje no encontrado"}
            return JsonResponse(datos)
        else:
            personajes= list(Personaje.objects.values())
            if len(personajes)>0:
                datos={'messaje':"Success", 'personajes':personajes}
            else:
                datos={'messaje':"Personajes no encontrados"}
            return JsonResponse(datos)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        personajes= list(Personaje.objects.filter(id=id).values())
        if len(personajes)>0:
            person=Personaje.objects.get(id=id)
            person.nombre=jd['nombre']
            person.save()
            datos = {'message': 'Succes'}
        else:
            datos={'messaje':"Personaje no encontrados"}
        return JsonResponse(datos)

    def delete(self,request,id):
        personajes= list(Personaje.objects.filter(id=id).values())
        if len(personajes)>0:
            Personaje.objects.filter(id=id).delete()
            datos = {'message': 'Succes'}
        else:
            datos={'messaje':"Personaje no encontrados"}
        return JsonResponse(datos)

class personajesviewadd(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        jd = json.loads(request.body)
        Personaje.objects.create(nombre=jd['nombre'])
        datos = {'message': 'Succes'}
        return JsonResponse(datos)

#VISTAS PARA PELICULAS

class peliculasview(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):

        if id > 0:
            pelis= list(peliculas.objects.filter(id=id).values())
            print(pelis)
            if len(pelis)>0:
                pl = pelis[0]
                datos={'messaje':"Success", 'pelicula':pl}
            else:
                datos={'messaje':"Pelicula no encontrada"}
            return JsonResponse(datos)
        else:
            pelis= list(peliculas.objects.values())
            if len(pelis)>0:
                datos={'messaje':"Success", 'peliculas':pelis}
            else:
                datos={'messaje':"Peliculas no encontradas"}
            return JsonResponse(datos)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        pelis= list(peliculas.objects.filter(id=id).values())
        if len(pelis)>0:
            pel=peliculas.objects.get(id=id)
            pel.nombre=jd['nombre']
            pel.director=jd['director'], 
            pel.productores=jd['productores'],
            pel.texto_apertura=jd['texto_apertura']
            pel.save()
            datos = {'message': 'Succes'}
        else:
            datos={'messaje':"Peliculas no encontradas"}
        return JsonResponse(datos)
    
    def delete(self,request,id):
        pelis= list(peliculas.objects.filter(id=id).values())
        if len(pelis)>0:
            peliculas.objects.filter(id=id).delete()
            datos = {'message': 'Succes'}
        else:
            datos={'messaje':"Pelicula no encontrada"}
        return JsonResponse(datos)

class peliculasviewadd(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self,request):
        jd = json.loads(request.body)
        peliculas.objects.create(nombre=jd['nombre'], 
        director=jd['director'], 
        productores=jd['productores'],
        texto_apertura=jd['texto_apertura'])
        
        datos = {'message': 'Succes'}
        return JsonResponse(datos)

#VISTAS PARA PLANETAS

class planetasview(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):

        if id > 0:
            planet= list(planeta.objects.filter(id=id).values())
            if len(planet)>0:
                pl = planet[0]
                datos={'messaje':"Success", 'planeta':pl}
            else:
                datos={'messaje':"Planeta no encontrado"}
            return JsonResponse(datos)
        else:
            planet= list(planeta.objects.values())
            if len(planet)>0:
                datos={'messaje':"Success", 'planetas':planet}
            else:
                datos={'messaje':"Planetas no encontrados"}
            return JsonResponse(datos)
    
    
    def put(self,request,id):
        jd = json.loads(request.body)
        planet= list(planeta.objects.filter(id=id).values())
        if len(planet)>0:
            pla=planeta.objects.get(id=id)
            pla.nombre=jd['nombre']
            pla.save()
            datos = {'message': 'Succes'}
        else:
            datos={'messaje':"Planeta no encontrado"}
        return JsonResponse(datos)
    
    def delete(self,request,id):
        
        planet= list(planeta.objects.filter(id=id).values())
        if len(planet)>0:
            planeta.objects.filter(id=id).delete()
            datos = {'message': 'Succes'}
        else:
            datos={'messaje':"Planeta no encontrado"}
        return JsonResponse(datos)

class planetasviewadd(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        jd = json.loads(request.body)
        planeta.objects.create(nombre=jd['nombre'])
        datos = {'message': 'Succes'}
        return JsonResponse(datos)