from django.shortcuts import render
from django.http import HttpResponse

from .models import Metodo

# Create your views here.

def home(request):
	#return HttpResponse('<h1>Holaaaa</h1>')
	return render(request, 'home.html', {'name':'Esneider Zapata Arias'})

def methods(request):
	searchTerm = request.GET.get('searchMethod')
	if searchTerm:
		metodos = Metodo.objects.filter(nombre__icontains=searchTerm)
	else:
		metodos = Metodo.objects.all()
	return render(request, 'methods.html', {'searchTerm':searchTerm, 'metodos':metodos})

def about(request):
	return HttpResponse('<h1>Holaaaa</h1>')