menu = """

    MENU
    1. Deposit
    2. Withdraw
    3. Balance
    4. New User
    5. New Account
    6. List Accounts
    7. Exit

"""

saldo = 0
limite = 500
operacoes = []
usuarios = []
contas = []


def tela():
    global menu
    print(menu)


def deposit(valor):
    global saldo
    if valor > 0:
        saldo += valor
        operacoes.append("Deposito: R$ {:.2f}".format(valor))
        print("Deposito Realizado")
    else:
        print("Valor inválido")


def withdraw(valor):
    global saldo
    global limite
    if valor > 0 and valor <= saldo and valor > limite:
        saldo -= valor
        operacoes.append("Saque: R$ {:.2f}".format(valor))
        print("Saque Realizado")
    else:
        print("Valor inválido")


def balance():
    global saldo
    print(f"\n================EXTRATO================")
    for operacao in operacoes:
        print(operacao)
        print("=======================================")
    print(f"Saldo: R$ {saldo:.2f}")


def filterUser(cpf):
    global usuarios
    for user in usuarios:
        if user["cpf"] == cpf:
            return user
        else:
            return False


def createUser(cpf, nome, dt_nasc):
    global usuarios
    if not filterUser(cpf):
        usuarios.append({"nome": nome, "cpf": cpf, "dt_nasc": dt_nasc})
    else:
        print("Usuário já cadastrado")


def createAccount(agencia, numero, usuario):
    global contas
    global usuarios
    if filterUser(usuario["cpf"]):
        contas.append({"agencia": agencia, "numero": numero, "usuario": usuario["cpf"]})
    else:
        print("Usuário não cadastrado")


def listAccounts():
    global contas
    for conta in contas:
        print(conta)


def Main():
    global contas
    global usuarios
    global operacoes
    global saldo
    global limite

    tela()
    while True:
        opcao = int(input("Digite a opcao desejada"))
        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            deposit(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            withdraw(valor)
        elif opcao == 3:
            balance()
        elif opcao == 4:
            cpf = input("Digite o cpf do usuário: ")
            nome = input("Digite o nome do usuário: ")
            dt_nasc = input("Digite a data de nascimento: ")
            createUser(cpf, nome, dt_nasc)
        elif opcao == 5:
            agencia = input("Digite a agencia: ")
            numero = input("Digite o numero da conta: ")
            cpf = input("Digite o cpf do usuário: ")
            if filterUser(cpf):
                usuario = filterUser(cpf)
                createAccount(agencia, numero, usuario)
            else:
                print("Usuário não cadastrado")
        elif opcao == 6:
            listAccounts()
        elif opcao == 7:
            break


Main()
