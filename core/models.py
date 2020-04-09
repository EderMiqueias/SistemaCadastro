from mongoengine import connect
from sistema.db import getdb
connect('mongo')


class Endereco:
    rua = None
    cep = None
    numero = None
    def __init__(self, rua=None, cep=None, numero=None):
        self.rua = rua
        self.cep = cep
        self.numero = numero
    def toJson(self):
        return {
            'rua': self.rua,
            'cep': self.cep,
            'numero': self.numero
        }
    def fromJason(self,data):
        return Endereco(
            rua=data['rua'],
            cep=data['cep'],
            numero=data['numero']
        )


class Cliente:
    id = None
    nome = None
    cpf = None
    endereco = None
    def __init__(self, mid=None, nome=None, cpf=None, endereco=None):
        self.mid = mid
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
    def toJson(self):
        return {
            'id': self.mid,
            'nome': self.nome,
            'cpf': self.cpf,
            'endereco': self.endereco.toJson()
        }
    def fromJson(self,data):
        end = data['endereco']
        return Cliente(
            mid=data['id'],
            nome=data['nome'],
            cpf=data['cpf'],
            endereco=Endereco(
                rua=end['rua'],
                cep=end['cep'],
                numero=end['numero']
            )
        )
    def fromCpf(self, cpf):
        db = getdb()
        cliente = db.clientes.find_one({'cpf':cpf})
        if cliente:
            cliente = self.fromJson(cliente)
            return cliente
        return 404
