from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	#return HttpResponse('<h1>Holaaaa</h1>')
	return render(request, 'home.html', {'name':'Esneider Zapata Arias'})

def methods(request):
	searchTerm = request.GET.get('searchMethod')
	return render(request, 'methods.html', {'searchTerm':searchTerm})

def about(request):
	return HttpResponse('<h1>Holaaaa</h1>')