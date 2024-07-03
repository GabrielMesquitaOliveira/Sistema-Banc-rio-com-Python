menu = '''

    MENU
    1. Deposit
    2. Withdraw
    3. Balance
    4. Exit

'''

saldo = 0
limite = 500
operacoes = []

while True:
    print(menu)
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        valor = float(input('Digite o valor a ser depositado: '))
        if valor < 0:
            print('Valor inválido')
        else:
            saldo += valor
        print('Deposito realizado com sucesso')
        operacao = {
            'tipo': 'deposito',
            'valor': valor,
        }
        operacoes.append(operacao)
    elif opcao ==2:
        valor = float(input('Digite o valor a ser sacado'))
        if valor > saldo:
            print('Saldo insuficiente')
        else:
            if valor > limite:
                print('Valor excede o limite')
            else:
                print('Saque realizado com sucesso')
                operacao = {
                    'tipo': 'saque',
                    'valor': valor,
                }
                operacoes.append(operacao)
    elif opcao == 3:
        print(f'\n================EXTRATO================')
        for operacao in operacoes:
            if operacao['tipo'] == 'deposito':
                print(f'Depósito de R${operacao["valor"]}')
            else:
                print(f'Saque de R${operacao["valor"]}')
    elif opcao == 4:
        print('Saindo do sistema')
        break
    else:
        print('Opção inválida')