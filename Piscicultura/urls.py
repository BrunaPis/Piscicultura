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
from django.urls import path


from app.views import home, form, create, view, edit, update, delete
from app.views import home2, form2, create2, view2, edit2, update2, delete2
from app.views import home3, form3, create3, view3, edit3, update3, delete3
from app.views import home4, form4, create4, view4, edit4, update4, delete4
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('', home2, name='home2'),
    path('form2/', form2, name='form2'),
    path('create2/', create2, name='create2'),
    path('view2/<int:pk>/', view2, name='view2'),
    path('edit2/<int:pk>/', edit2, name='edit2'),
    path('update2/<int:pk>/', update2, name='update2'),
    path('delete2/<int:pk>/', delete2, name='delete2'),
    path('', home3, name='home3'),
    path('form3/', form3, name='form3'),
    path('create3/', create3, name='create3'),
    path('view3/<int:pk>/', view3, name='view3'),
    path('edit3/<int:pk>/', edit3, name='edit3'),
    path('update3/<int:pk>/', update3, name='update3'),
    path('delete3/<int:pk>/', delete3, name='delete3'),
    path('', home4, name='home4'),
    path('form4/', form4, name='form4'),
    path('create4/', create4, name='create4'),
    path('view4/<int:pk>/', view4, name='view4'),
    path('edit4/<int:pk>/', edit4, name='edit4'),
    path('update4/<int:pk>/', update4, name='update4'),
    path('delete4/<int:pk>/', delete4, name='delete4'),
]