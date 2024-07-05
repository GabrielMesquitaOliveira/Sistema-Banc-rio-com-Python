from datetime import datetime


# Sistema bancario
class Transacao:
    def __init__(self, valor, tipo):
        self._valor = valor
        self._tipo = tipo

    @property
    def valor(self):
        return self._valor

    @property
    def tipo(self):
        return self._tipo


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente: Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar(cls, numero, cliente: Cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            transacao = Transacao(valor, "Deposito")
            self._historico.adicionar(transacao)
            print("deposito realizado")
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            transacao = Transacao(valor, "Saque")
            self._historico.adicionar(transacao)
            print("Saque realizado")
        else:
            print("Saldo insuficiente")


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar(self, transacao:Transacao):
        self._transacoes.append(
            {"data": datetime.now(), "valor": transacao.valor, "tipo": transacao.tipo}
        )

    @property
    def transacoes(self):
        return self._transacoes


menu = """

    MENU
    1. Deposit
    2. Withdraw
    3. Balance
    4. New User
    5. New Account
    7. Exit

"""
cliente = ""
conta = ""


def tela():
    global menu
    print(menu)


def Main():
    tela()
    global cliente
    global conta

    while True:
        opcao = int(input("Digite a opcao desejada"))
        if opcao == 1:
            valor = int(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)

        elif opcao == 2:
            valor = int(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)

        elif opcao == 3:
            operacoes = conta.historico.transacoes
            print(f"\n================EXTRATO================")
            for operacao in operacoes:
                print(operacao)
                print("=======================================")

        elif opcao == 4:
            endereco = input("Digite seu endereco: ")
            cliente = Cliente(endereco)
            print("cliente criado com sucesso")

        elif opcao == 5:
            numero = input("Digite o numero de sua nova conta: ")
            conta = Conta(numero, cliente)
            print("conta criada com sucesso")

        elif opcao == 7:
            break


Main()
