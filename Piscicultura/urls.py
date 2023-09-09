"""
URL configuration for Piscicultura Piscicultura.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from app.viewsets import PiscicultoresViewSet, ViveirosViewSet, PeixesViewSet,RacaoViewSet

router = routers.DefaultRouter()
router.register(r'Piscicultores', PiscicultoresViewSet, basename="Piscicultores")
router.register(r'Viveiros', ViveirosViewSet, basename="Viveiros")
router.register(r'Peixes', PeixesViewSet, basename="Peixes")
router.register(r'Racao', RacaoViewSet, basename="Racao")


from app.views import create_piscicultor,viewspiscicultor, editPiscicultor, updatePiscicultor, IndexPiscicultor, deletePiscicultor
from app.views import create_viveiro,viewsviveiro,editViveiro,updateViveiro,deleteViveiro,IndexViveiro
from app.views import home,login,Index,create_peixe,viewspeixe,updatePeixe,editPeixe,deletePeixe,IndexPeixe
from app.views import viewspiscicultor,viewsracao,create_racao,updateRacao,editRacao,deleteRacao,IndexRacao, cep
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path("api/", include(router.urls)),
    path('cep/', cep, name='cep'),
    path('create_piscicultor/',create_piscicultor, name='create_piscicultor'),
    path('viewspiscicultor/<int:pk>/', viewspiscicultor, name='viewspiscicultor'),
    path('editPiscicultor/<int:pk>/', updatePiscicultor, name='editPiscicultor'),
    path('updatePiscicultor/<int:pk>/', updatePiscicultor, name='updatePiscicultor'),
    path('deletePiscicultor/<int:pk>/', deletePiscicultor, name='deletePiscicultor'),
    path('IndexPiscicultor/', IndexPiscicultor, name='IndexPiscicultor'),

    path('create_viveiro/', create_viveiro, name='create_viveiro'),
    path('viewsviveiro/<int:pk>/',viewsviveiro, name='viewsviveiro'),
    path('editViveiro/<int:pk>/', editViveiro, name='editViveiro'),
    path('updateViveiro/<int:pk>/', updateViveiro, name='updateViveiro'),
    path('deleteViveiro/<int:pk>/', deleteViveiro, name='deleteViveiro'),
    path('IndexViveiro/', IndexViveiro, name='IndexViveiro'),


    path('create_peixe/', create_peixe, name='create_peixe'),
    path('viewspeixe/<int:pk>/', viewspeixe, name='viewspeixe'),
    path('editPeixe/<int:pk>/', editPeixe, name='editPeixe'),
    path('updatePeixe/<int:pk>/', updatePeixe, name='updatePeixe'),
    path('deletePeixe/<int:pk>/', deletePeixe, name='deletePeixe'),
    path('IndexPeixe/', IndexPeixe, name='IndexPeixe'),

    path('create_racao/',create_racao, name='create_racao'),
    path('viewsracao/<int:pk>/', viewsracao, name='viewsracao'),
    path('editRacao/<int:pk>/', editRacao, name='editRacao'),
    path('updateRacao/<int:pk>/', updateRacao, name='updateRacao'),
    path('deleteRacao/<int:pk>/', deleteRacao, name='deleteRacao'),
    path('IndexRacao/', IndexRacao, name='IndexRacao'),




]