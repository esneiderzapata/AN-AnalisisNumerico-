"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AnalisisNumerico import views as ANviews

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ANviews.home),
    path('about/', ANviews.about),
    path('methods/', ANviews.methods),
    path('Biseccion/', ANviews.biseccion),
    path('PuntoFijo/', ANviews.puntofijo),
    path('ReglaFalsa/', ANviews.reglafalsa),
    path('NewtonRaphson/', ANviews.newtonraphson),
    path('Secante/', ANviews.secante),
    path('GaussJordan/', ANviews.gaussjordan),
    path('GaussSeidel/', ANviews.gaussseidel),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)