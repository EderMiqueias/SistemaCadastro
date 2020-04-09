from django import forms
from .models import Endereco, Cliente
from sistema.db import getdb

class ClienteModelForm(forms.Form):
    id = forms.CharField(label='Id', max_length=3)
    nome = forms.CharField(label='Nome', max_length=60)
    cpf = forms.CharField(label='CPF', max_length=11)
    rua = forms.CharField(label="Rua", max_length=100)
    cep = forms.IntegerField(label='CEP')
    numero = forms.IntegerField(label='Numero')
    db = getdb()
    def salvar(self):
        endereco = Endereco(
            rua=self.cleaned_data['rua'],
            cep=self.cleaned_data['cep'],
            numero=self.cleaned_data['numero']
        )
        cliente = Cliente(
            mid=self.cleaned_data['id'],
            cpf=self.cleaned_data['cpf'],
            nome=self.cleaned_data['nome'],
            endereco=endereco
        )
        print("Cliente registrado como:",cliente.nome)
        self.db.clientes.insert_one(
            cliente.toJson()
        )
    def verificar_cpf(self,cpf):
        for cliente in self.db.clientes.find():
            if cpf == cliente['cpf']:
                return True
        return False
