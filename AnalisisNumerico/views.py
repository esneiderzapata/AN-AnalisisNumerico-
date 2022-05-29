from django.shortcuts import render
from django.http import HttpResponse

from .models import Metodo

from sympy import *

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

def biseccion(request):
	x = symbols('x') 
	exp = sin(x)
	xi = 0
	xs = 1
	_type = 0
	tol = 0.5*10**-3
	_iter = 10
	
	if request.method == 'POST':
		exp = request.POST.get('txtFUN')
		xi = request.POST.get('txtXI')
		xs = request.POST.get('txtXS')
		_type = request.POST.get('txtTYPE')
		tol = request.POST.get('txtTOL')
		_iter = request.POST.get('txtITER')

	f = lambdify(x, exp, "math")

	return render(request, 'biseccion.html')
		

def about(request):
	return HttpResponse('<h1>Holaaaa</h1>')