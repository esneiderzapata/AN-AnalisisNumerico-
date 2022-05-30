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
	error = 9999
	iterActual = 0
	
	x = symbols('x') 
	exp = cos(x)-x**3
	xi = 0
	xs = pi
	_type = 0
	tol = 10**-6
	_iter = 100

	tablaBiseccion = [[]]
	auxi = 0
	auxs = 0

	if request.method == 'POST':
		tablaBiseccion.clear()
		exp = request.POST.get('txtFUN')
		xi = eval(request.POST.get('txtXI'))
		xs = eval(request.POST.get('txtXS'))
		_type = eval(request.POST.get('txtTYPE'))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	tablaBiseccion = [['Iter','xi','xs','xmedio','F(xi)','F(xs)','F(xmedio)','Error']]

	f = lambdify(x, exp, "math")
	print(xi," / ", xs," / ", _type," / ", tol)

	if(f(xi)*f(xs)<0):
		while (abs(error)>tol) and (iterActual<_iter):

			auxi = xi
			auxs = xs
			puntoMedio = (xi+xs)/2

			if (f(xi)*f(puntoMedio)<0): #Cambio de Signo en [xi,puntoMedio]
				xs = puntoMedio
			elif (f(puntoMedio)*f(xs)<0): #Cambio de Signo en [puntoMedio,xs]
				xi = puntoMedio
			#print ('El intervalo es [',xi,',',xs,']')
	
			iterActual += 1
			if (_type==0):
				error = xs-xi
			else:
				error = (xs-xi)/xs

			tablaBiseccion.append([(iterActual),f"{float(auxi):.3f}",f"{float(auxs):.3f}",f"{float(puntoMedio):.3f}",f"{float(f(xi)):.3f}",f"{float(f(xs)):.3f}",f"{float(f(puntoMedio)):.3f}",f"{float(error):.6f}"])

	#print ('x',iterActual, '=',float(puntoMedio),' es una buena aproximacion')
	return render(request, 'biseccion.html', {'iterActual':iterActual, 'puntoMedio':float(puntoMedio), 'tablaBiseccion':tablaBiseccion, 'exp':exp})

def puntofijo(request):
	error = 9999
	iterActual = 0
	
	x = symbols('x') 
	exp = cos(x)-x**3
	xi = 0
	xs = pi
	_type = 0
	tol = 10**-6
	_iter = 100

	tablaBiseccion = [[]]
	auxi = 0
	auxs = 0

	if request.method == 'POST':
		tablaBiseccion.clear()
		exp = request.POST.get('txtFUN')
		xi = eval(request.POST.get('txtXI'))
		xs = eval(request.POST.get('txtXS'))
		_type = eval(request.POST.get('txtTYPE'))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	tablaBiseccion = [['Iter','xi','xs','xmedio','F(xi)','F(xs)','F(xmedio)','Error']]

	f = lambdify(x, exp, "math")
	print(xi," / ", xs," / ", _type," / ", tol)

	if(f(xi)*f(xs)<0):
		while (abs(error)>tol) and (iterActual<_iter):

			auxi = xi
			auxs = xs
			puntoMedio = (xi+xs)/2

			if (f(xi)*f(puntoMedio)<0): #Cambio de Signo en [xi,puntoMedio]
				xs = puntoMedio
			elif (f(puntoMedio)*f(xs)<0): #Cambio de Signo en [puntoMedio,xs]
				xi = puntoMedio
			#print ('El intervalo es [',xi,',',xs,']')
	
			iterActual += 1
			if (_type==0):
				error = xs-xi
			else:
				error = (xs-xi)/xs

			tablaBiseccion.append([(iterActual),f"{float(auxi):.3f}",f"{float(auxs):.3f}",f"{float(puntoMedio):.3f}",f"{float(f(xi)):.3f}",f"{float(f(xs)):.3f}",f"{float(f(puntoMedio)):.3f}",f"{float(error):.6f}"])

	#print ('x',iterActual, '=',float(puntoMedio),' es una buena aproximacion')
	return render(request, 'puntofijo.html', {'iterActual':iterActual, 'puntoMedio':float(puntoMedio), 'tablaBiseccion':tablaBiseccion, 'exp':exp})
		

def about(request):
	return HttpResponse('<h1>Holaaaa</h1>')