from django.urls import path
from .views import crear,leer,update

urlpatterns = [
    path('', crear,name='crear'), 
    path('leer/', leer, name='leer'),
    path('update/',update,name='update'), 
] 