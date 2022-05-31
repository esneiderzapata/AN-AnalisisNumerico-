from django.shortcuts import render
from django.http import HttpResponse

from .models import Metodo

from math import *
from sympy import *
import sympy as sp
import numpy as np

# Create your views here.

def home(request):
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

	if(f(xi)*f(xs)<=0):
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
	exp = cos(x)
	x0 = pi/2
	_type = 0
	tol = 10**-4
	_iter = 50

	tablaPuntoFijo = [[]]
	auxi = 0
	auxs = 0

	if request.method == 'POST':
		tablaPuntoFijo.clear()
		exp = request.POST.get('txtFUN')
		x0 = eval(request.POST.get('txtX0'))
		_type = eval(request.POST.get('txtTYPE'))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	tablaPuntoFijo = [['Iter','xn','g(n)','Error']]

	g = lambdify(x, exp, "math")

	while (abs(error)>tol) and (iterActual<_iter):
		x1 = g(x0)
		
		if (_type==0):
			error = x1-x0
		else:
			error = (x1-x0)/x1

		iterActual += 1
		tablaPuntoFijo.append([(iterActual),f"{float(x0):.3f}",f"{float(g(x0)):.3f}",f"{float(error):.6f}"])
		
		if (abs(error)<tol):
			break
		else:
			x0 = x1

	return render(request, 'puntofijo.html', {'iterActual':iterActual, 'x1':x1, 'tablaPuntoFijo':tablaPuntoFijo, 'exp':exp})

def reglafalsa(request):
	error = 9999
	iterActual = 0

	solucion = None
	
	x = symbols('x') 
	exp = 4*x**4-9*x**2+1
	xi = 0
	xs = 1
	_type = 1
	tol = 0.001
	_iter = 1000

	tablaReglaFalsa = [[]]
	auxi = 0
	auxs = 0

	if request.method == 'POST':
		tablaReglaFalsa.clear()
		exp = request.POST.get('txtFUN')
		xi = eval(request.POST.get('txtXI'))
		xs = eval(request.POST.get('txtXS'))
		_type = eval(request.POST.get('txtTYPE'))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	tablaReglaFalsa = [['Iter','xi','xs','xr','Error']]

	f = lambdify(x, exp, "math")
	
	#Evaluar si la raiz esta dentro del intervalo
	if (f(xi)*f(xs)<=0):
		#Calcular la solucion
		while (abs(error)>tol) and (iterActual<_iter):
			iterActual += 1
			solucion = float(xs - ((f(xs)*(xs-xi)) / (f(xs)-f(xi))))

			if (_type==0):
				error = solucion-xi
			else:
				error = (solucion-xi)/solucion

			tablaReglaFalsa.append([(iterActual),f"{float(xi):.3f}",f"{float(xs):.3f}",f"{float(solucion):.3f}",f"{float(error):.6f}"])

			#Redefinir el nuevo intervalo
			if (f(xi)*f(solucion))>=0:
				xi = solucion
			else:
				xs = solucion


	return render(request, 'reglafalsa.html', {'iterActual':iterActual, 'solucion':solucion, 'tablaReglaFalsa':tablaReglaFalsa, 'exp':exp})
		
def newtonraphson(request):
	error = 9999
	iterActual = 0
	
	x = symbols('x') 
	exp = cos(x)-x**3
	x0 = pi
	_type = 0
	tol = 0.0001
	_iter = 10

	tablaNewtonRaphson = [[]]
	auxi = 0
	auxs = 0

	if request.method == 'POST':
		tablaNewtonRaphson.clear()
		exp = request.POST.get('txtFUN')
		x0 = eval(request.POST.get('txtX0'))
		_type = eval(request.POST.get('txtTYPE'))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	tablaNewtonRaphson = [['Iter','xn','xn-f(xn)/df(xn)','Error']]

	f = lambdify(x, exp, "math")
	df= lambdify(x, sp.diff(exp), "math")

	while (abs(error)>tol) and (iterActual<_iter):
		x1 = float(x0-f(x0)/df(x0))
		
		if (_type==0):
			error = x1-x0
		else:
			error = (x1-x0)/x1
	
		iterActual += 1
		tablaNewtonRaphson.append([(iterActual),f"{float(x0):.3f}",f"{float(x1):.3f}",f"{float(error):.6f}"])
		
		if (abs(error)<tol):
			break
		else:
			x0 = x1
	
	return render(request, 'newtonraphson.html', {'iterActual':iterActual, 'x1':x1, 'tablaNewtonRaphson':tablaNewtonRaphson, 'exp':exp, 'df':sp.diff(exp)})

def secante(request):
	error = 9999
	iterActual = 0
	
	x = symbols('x') 
	exp = x**2-10
	x0 = 11
	x1 = 10
	tol = 10**-7
	_iter = 10

	tablaSecante = [[]]
	auxi = 0
	auxs = 0

	if request.method == 'POST':
		tablaSecante.clear()
		exp = request.POST.get('txtFUN')
		x0 = eval(request.POST.get('txtX0'))
		x1 = eval(request.POST.get('txtX1'))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	tablaSecante = [['Iter','xn','xn+1','xn+2','Error']]

	f = lambdify(x, exp, "math")

	while (abs(error)>tol) and (iterActual<_iter):
		x2 = float(x0-((x1-x0)/(f(x1)-f(x0)))*f(x0))

		error = f(x2)
		iterActual += 1

		tablaSecante.append([(iterActual),f"{float(x0):.3f}",f"{float(x1):.3f}",f"{float(x2):.3f}",f"{float(error):.6f}"])

		x0 = x1
		x1 = x2

	return render(request, 'secante.html', {'iterActual':iterActual, 'x2':x2, 'tablaSecante':tablaSecante, 'exp':exp})

def gaussjordan(request):

	A = np.array([[4,2,5],[2,5,8],[5,4,3]])
	B = np.array([[60.70],[92.90],[56.30]])
	T = 1

	if request.method == 'POST':
		A = np.array(descifradorMatrices(str(request.POST.get('txtA'))))
		B = np.array(descifradorMatrices(str(request.POST.get('txtB'))))
		T = int(request.POST.get('txtPIV'))

	ABoriginal = np.concatenate((A,B),axis=1)
	casicero = 1e-15

	# Evitar truncamiento en operaciones
	A = np.array(A,dtype=float) 

	# Matriz aumentada
	AB  = np.concatenate((A,B),axis=1)
	AB0 = np.copy(AB)

	# Pivoteo parcial por filas
	tamano = np.shape(AB)
	n = tamano[0]
	m = tamano[1]
	if T==1:
		# Para cada fila en AB
		for i in range(0,n-1,1):
			# columna desde diagonal i en adelante
			columna  = abs(AB[i:,i])
			dondemax = np.argmax(columna)
    
			# dondemax no está en diagonal
			if (dondemax !=0):
				# intercambia filas
				temporal = np.copy(AB[i,:])
				AB[i,:] = AB[dondemax+i,:]
				AB[dondemax+i,:] = temporal
	AB1 = np.copy(AB)

	# eliminación hacia adelante
	for i in range(0,n-1,1):
		pivote   = AB[i,i]
		adelante = i + 1
		for k in range(adelante,n,1):
			factor  = AB[k,i]/pivote
			AB[k,:] = AB[k,:] - AB[i,:]*factor

	# sustitución hacia atrás
	ultfila = n-1
	ultcolumna = m-1
	X = np.zeros(n,dtype=float)

	for i in range(ultfila,0-1,-1):
		suma = 0
		for j in range(i+1,ultcolumna,1):
			suma = suma + AB[i,j]*X[j]
		b = AB[i,ultcolumna]
		X[i] = (b-suma)/AB[i,i]

	X = np.transpose([X])
	
	return render(request, 'gaussjordan.html', {'ABoriginal':ABoriginal, 'AB':AB1, 'A':A, 'B':B, 'X':X})

def gaussseidel(request):

	A = np.array([[3.,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
	B = np.array([[7.85],[-19.3],[71.4]])
	x0 = np.array([0.0,0,0])

	tol = 0.0001
	_iter = 100
	
	error = 9999
	iterActual = 0

	if request.method == 'POST':
		A = np.array(descifradorMatrices(str(request.POST.get('txtA'))))
		B = np.array(descifradorMatrices(str(request.POST.get('txtB'))))
		x0 = np.array(descifradorMatrices(str(request.POST.get('txtX0'))))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	tabla = [['Iter','Solucion','Error']]
	tamano = np.shape(A)
	n = tamano[0]
	m = tamano[1]

	X = np.copy(x0)
	diferencia = np.ones(n, dtype = float)

	i=0

	while (abs(error)>tol) and (iterActual<_iter):
		for i in range(0,n,1):
			suma = 0
			for j in range(0,n,1):
				if (j != i):
					suma = suma + A[i,j]*X[j]
			nuevo = (B[i] - suma)/A[i,i]
			diferencia[i] = np.abs(nuevo-X[i])
			X[i] = nuevo
		
		error = np.max(diferencia)
		iterActual += 1
		tabla.append([iterActual, X, f"{float(error):.6f}"])

	return render(request, 'gaussseidel.html', {'X':X, 'iterActual':iterActual, 'tabla':tabla, 'error':error})

def jacobi(request):

	A = np.array([[3.,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
	B = np.array([7.85,-19.3,71.4])
	x0 = np.array([0.0,0,0])

	tol = 0.0001
	_iter = 100
	
	error = 9999
	iterActual = 0

	if request.method == 'POST':
		A = np.array(descifradorMatrices(str(request.POST.get('txtA'))))
		B = np.array(descifradorMatrices(str(request.POST.get('txtB'))))
		x0 = np.array(descifradorMatrices(str(request.POST.get('txtX0'))))
		tol = eval(request.POST.get('txtTOL'))
		_iter = eval(request.POST.get('txtITER'))

	D=np.diag(np.diag(A))
	LU=A-D
	X=x0
	for i in range(_iter):
		D_inv=np.linalg.inv(D)
		xtemp=X
		X=np.dot(D_inv,np.dot(-LU,X))+np.dot(D_inv,B)
		error = np.linalg.norm(X-xtemp)
		iterActual+=1
		if error<tol:
			break

	return render(request, 'jacobi.html', {'X':X, 'iterActual':iterActual, 'error':error})

def spline(request):

	X = np.array([-3,-1,1,2])
	Y = np.array([6,2,-1,3])
	T = 1
	Tabla = [[]]

	if request.method == 'POST':
		X = np.array(descifradorMatrices(str(request.POST.get('txtX'))))
		Y = np.array(descifradorMatrices(str(request.POST.get('txtY'))))
		T = eval(request.POST.get('txtT'))

	n=len(X)
	
	if (T==1):
		Tabla=[['mx','b']]
		for k in range(n-1):
			m=(Y[k+1]-Y[k])/(X[k+1]-X[k])
			b=Y[k]-m*X[k]
			Tabla.append([f"{float(m):.3f}",f"{float(b):.3f}"])

	elif(T==3):
		Tabla=[['ax^3','bx^2','cx','d']]
		A=np.array(np.zeros([(T+1)*(n-1),(T+1)*(n-1)]))
		b=np.array(zeros((T+1)*(n-1),1))
		cua=np.array(np.multiply(X,X))
		cub=np.array(np.multiply(cua,X))
		c=1
		h=1
		for i in range(1,n):
			A[i-1,c-1]=cub[i-1]
			A[i-1,c+1-1]=cua[i-1]
			A[i-1,c+2-1]=X[i-1]
			A[i-1,c+3-1]=1
			b[i-1]=Y[i-1]
			c=c+4
			h=h+1

		c=1
		for i in range(2,n+1):
			A[h-1,c-1]=cub[i-1]
			A[h-1,c+1-1]=cua[i-1]
			A[h-1,c+2-1]=X[i-1]
			A[h-1,c+3-1]=1
			b[h-1]=Y[i-1]
			c=c+4
			h=h+1

		c=1
		for i in range(2,n):
			A[h-1,c-1]=3*cua[i-1]
			A[h-1,c+1-1]=2*X[i-1]
			A[h-1,c+2-1]=1
			A[h-1,c+4-1]=-3*cua[i-1]
			A[h-1,c+5-1]=-2*X[i-1]
			A[h-1,c+6-1]=-1
			b[h-1]=0
			c=c+4
			h=h+1

		c=1
		for i in range(2,n):
			A[h-1,c-1]=6*X[i-1]
			A[h-1,c+1-1]=2
			A[h-1,c+4-1]=-6*X[i-1]
			A[h-1,c+5-1]=-2
			b[h-1]=0
			c=c+4
			h=h+1

		A[h-1,1-1]=6*X[0]
		A[h-1,2-1]=2
		b[h-1]=0
		h=h+1
		A[h-1,c-1]=6*X[-1]
		A[h-1,c+1-1]=2
		b[h-1]=0

		val = np.dot(np.linalg.inv(A),b)
		Tablatemp = np.reshape(val,[T+1,n-1],order='F')
		Tablatemp = np.transpose(Tablatemp)
		
		for lista in Tablatemp:
			Tabla.append(lista)

	return render(request, 'spline.html',{'Tabla':Tabla})

def vandermonde(request):

	X = np.array([1,2,3])
	Y = np.array([2,0,1])
	Tabla=[[]]

	if request.method == 'POST':
		X = np.array(descifradorMatrices(str(request.POST.get('txtX'))))
		Y = np.array(descifradorMatrices(str(request.POST.get('txtY'))))

	n=len(X)
	X2 = np.ones([n,n])
	
	for i in range(1,n+1):
		for m in range(1,n):
			X2[i-1,m-1]= (X[i-1]**(n-m))

	solucion = np.dot(np.linalg.inv(X2),Y)
	return render(request, 'vandermonde.html',{'Tabla':X2, 'solucion':solucion})

def about(request):
	return HttpResponse('<h1>Holaaaa</h1>', {'g':g})

def pivparcial(A,B):
	AB = np.concatenate((A,B),axis=1) #Matriz Aumentada
	ABoriginal = np.concatenate((A,B),axis=1)
	
	#Pivoteo Parcial por Filas
	tamano = np.shape(AB)
	n = tamano[0]#Filas
	m = tamano[1]#Columnas

	for i in range(0,n-1):
		columna= abs(AB[i:,i])
		dondemax = np.argmax(columna)
	
		#Intercambio de Filas
		if (dondemax != 0):
			temporal = np.copy(AB[i,:])
			AB[i,:] = AB[dondemax + i,:]
			AB[dondemax + i,:] = temporal

	return AB


def descifradorMatrices(matrizCifrada):
	lista = matrizCifrada.split()
	sublista = []
	matrizDescifrada = []
	cont = 0
	memoria = 0
	XD = False

	for x in lista:
		if (x != '#'):
			sublista.append(float(x))
			cont += 1
		else:
			XD = True
			matrizDescifrada.append(sublista[memoria:cont])
			memoria = cont
			
	matrizDescifrada.append(sublista[memoria:cont+1])

	if XD:
		return matrizDescifrada
	else:
		return sublista

