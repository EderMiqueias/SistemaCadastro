from django.shortcuts import render, redirect
from .forms import ClienteModelForm


def index(request):
    return redirect("home")


def home(request):
    return render(request,"index.html")


def cadastrar(request):
    formclient = ClienteModelForm(request.POST or None)
    verificar_cpf = False
    if str(request.method) == "POST":
        if formclient.is_valid():
            verificar_cpf = formclient.verificar_cpf(formclient.cleaned_data['cpf'])
            if not verificar_cpf:
                formclient.salvar()
                formclient = ClienteModelForm()
    context = {
        'formclient': formclient,
        'verificar_cpf': verificar_cpf
    }
    return render(request, 'cadastrar.html', context)

def buscar(request):
    return render(request,"buscar.html")


def editar(request):
    return render(request,"editar.html")


def buscarcep(request):
    return render(request,"buscarcep.html")


def ruas(request):
    return render(request,"ruas.html")


def backup(request):
    return render(request,"backup.html")
