from django import forms
from .models import Endereco, Cliente
from sistema.db import getdb


class ModeloCharField(forms.CharField):
    def __init__(self, name, ml):
        super().__init__(max_length=ml, label='', widget=forms.TextInput(
            attrs={'placeholder': f'{name}', 'style': 'margin: 1% 0'}
        ))


class ClienteModelForm(forms.Form):
    mid = ModeloCharField('Id', 3)
    nome = ModeloCharField('Nome', 60)
    cpf = ModeloCharField('CPF', 11)
    rua = ModeloCharField('Rua', 100)
    cep = ModeloCharField('CEP', 8)
    numero = ModeloCharField('N°', 4)
    db = getdb()

    def salvar(self):
        endereco = Endereco(
            rua=self.cleaned_data['rua'],
            cep=self.cleaned_data['cep'],
            numero=self.cleaned_data['numero']
        )
        cliente = Cliente(
            mid=self.cleaned_data['mid'],
            cpf=self.cleaned_data['cpf'],
            nome=self.cleaned_data['nome'],
            endereco=endereco
        )
        print("Cliente registrado como:", cliente.nome)
        self.db.clientes.insert_one(
            cliente.toJson()
        )

    def verificarCpf(self, cpf):
        for cliente in self.db.clientes.find():
            if cpf == cliente['cpf']:
                return True
        return False
