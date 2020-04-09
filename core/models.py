from mongoengine import connect
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
    def fromJason(self,data):
        return Cliente(
            mid=data['mid'],
            nome=data['nome'],
            cpf=data['cpf'],
            endereco=data['endereco']
        )