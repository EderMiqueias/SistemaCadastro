from django.urls import path
from .views import (index, cadastrar, buscar,
    editar, buscarcep, ruas, home
)

urlpatterns = [
    path("",index,name="index"),
    path("home/",home,name="home"),
    path("cadastrar/",cadastrar,name="cadastrar"),
    path("buscar/",buscar,name="buscar"),
    path("editar/",editar,name="editar"),
    path("buscarcep/",buscarcep,name="buscarcep"),
    path("ruas/",ruas,name="ruas")
]
