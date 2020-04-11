from django.shortcuts import render, redirect
from .forms import ClienteModelForm
from .models import Cliente, Endereco
from sistema.db import getdb

def index(request):
    return redirect("home")


def home(request):
    return render(request,"index.html")


def cadastrar(request):
    formclient = ClienteModelForm(request.POST or None)
    verificar_cpf = False
    if str(request.method) == "POST":
        if formclient.is_valid():
            verificar_cpf = formclient.verificarCpf(formclient.cleaned_data['cpf'])
            if not verificar_cpf:
                formclient.salvar()
                formclient = ClienteModelForm()
    context = {
        'formclient': formclient,
        'verificar_cpf': verificar_cpf
    }
    return render(request, 'cadastrar.html', context)


def buscar(request):
    cliente = None
    if str(request.method) == "POST":
        cpf = request.POST['cpf']
        cliente = Cliente().fromCpf(cpf)
    content = {
        'cliente': cliente,
        'endereco': cliente.endereco if isinstance(cliente,Cliente) else None,
        'url_atual': 'buscar'
    }
    return render(request,"buscar.html",content)


def editar(request):
    cliente = None
    formclient = None
    old_cpf = None
    if str(request.method) == "POST":
        cpf = request.POST['cpf']
        cliente = Cliente().fromCpf(cpf)
        if len(request.POST) == 2:
            formclient = ClienteModelForm(cliente)
            old_cpf = cpf
        if len(request.POST) == 8:
            db = getdb()
            cliente = None
            endereco_local = Endereco(
                rua=request.POST['rua'],
                cep=request.POST['cep'],
                numero=request.POST['numero']
            )
            cliente_local = Cliente(
                mid=request.POST['mid'],
                nome=request.POST['nome'],
                cpf=request.POST['cpf'],
                endereco=endereco_local
            )
            old_cpf = request.POST['old_cpf']
            db.clientes.update_one(
                {'cpf': old_cpf}, {"$set": cliente_local.toJson()}
            )
    content = {
        'formclient': formclient,
        'url_atual': 'editar',
        'cliente': cliente,
        'old_cpf': old_cpf
    }
    return render(request,"editar.html", content)


def buscarcep(request):
    return render(request,"buscarcep.html")


def ruas(request):
    return render(request,"ruas.html")


def backup(request):
    return render(request,"backup.html")
