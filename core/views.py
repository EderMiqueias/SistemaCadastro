from django.shortcuts import render, redirect
from django.contrib.staticfiles.views import serve
from .forms import ClienteModelForm
from .models import Cliente, Endereco
from sistema.db import getdb
import json


def index(request):
    return redirect("home")


def home(request):
    return render(request,"index.html")


def cadastrar(request):
    formclient = ClienteModelForm(request.POST or None)
    verificar_cpf = False
    salvo = False
    if str(request.method) == "POST":
        if formclient.is_valid():
            verificar_cpf = formclient.verificarCpf(formclient.cleaned_data['cpf'])
            if not verificar_cpf:
                formclient.salvar()
                formclient = ClienteModelForm()
                salvo = True
    context = {
        'formclient': formclient,
        'verificar_cpf': verificar_cpf,
        'salvo': salvo
    }
    return render(request, 'cadastrar.html', context)


def gerar_arquivo_cliente(cliente):
    arq = open(f"core/static/clientes/cliente_{cliente.cpf}.json", 'w')
    json.dump(cliente.toJson(), arq, indent=4)
    arqroot = open(f"staticroot/clientes/cliente_{cliente.cpf}.json", 'w')
    json.dump(cliente.toJson(), arqroot, indent=4)


def buscar(request):
    cliente = None
    cliente_download = None
    if str(request.method) == "POST":
        cpf = request.POST['cpf']
        cliente = Cliente().fromCpf(cpf)
        if isinstance(cliente, Cliente):
            gerar_arquivo_cliente(cliente)
            cliente_download = f"clientes/cliente_{cliente.cpf}.json"
    content = {
        'cliente': cliente,
        'endereco': cliente.endereco if isinstance(cliente, Cliente) else None,
        'url_atual': 'buscar',
        'cliente_download': cliente_download
    }
    return render(request,"buscar.html",content)


def editar(request):
    cliente = None
    formclient = None
    old_cpf = None
    sucesso_alterado = False
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
            sucesso_alterado = True
    content = {
        'formclient': formclient,
        'url_atual': 'editar',
        'cliente': cliente,
        'old_cpf': old_cpf,
        'sucesso_alterado':sucesso_alterado
    }
    return render(request,"editar.html", content)


def buscarcep(request):
    clientes = list()
    db = getdb()
    found = True
    if str(request.method) == "POST":
        cep = request.POST['cep']
        lista_importacoes = db.clientes.find()
        for cliente in lista_importacoes:
            if str(cliente['endereco']['cep']) == cep:
                clientes.append(cliente)
        if not clientes:
            found = False
    content = {
        'clientes': clientes,
        'found': found
    }
    return render(request,"buscarcep.html",content)


def ruas(request):
    enderecos = list()
    ruas = list()
    db = getdb()
    lista_importacoes = db.clientes.find()
    for cliente in lista_importacoes:
        rua = cliente['endereco']['rua']
        if not rua in ruas:
            enderecos.append(cliente['endereco'])
            ruas.append(rua)
    content = {
        'enderecos': enderecos
    }
    return render(request,"ruas.html", content)
