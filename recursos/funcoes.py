def depositar(saldoConta, listaExtrato):
    try:
        print()
        depositarDinheiro=float(input("Quanto você deseja depositar: "))
    except ValueError:
        print("Digite apenas números!")
        return saldoConta
    if depositarDinheiro<=0:
        print("Valor inválido!")
        return saldoConta
    saldoConta+=depositarDinheiro
    print()
    print(f"""Depósito realizado!

Saldo: R${saldoConta}
                  """)
    listaExtrato.append(f" + Depósito: R${depositarDinheiro}")
    return saldoConta

def saque(saldoConta,limiteSaque,listaExtrato):
    if limiteSaque==3:
        print("Limite de saque atingido!")
        return saldoConta,limiteSaque
    try:
        print()
        sacarDinheiro=float(input("Quanto você deseja sacar? "))
    except ValueError:
        print()
        print("Digite apenas números!")
        return saldoConta, limiteSaque
    if sacarDinheiro<=0:
        print()
        print("Valor inválido!")
    elif sacarDinheiro>500:
        print()
        print("O limite por saque é de R$500.")
    elif saldoConta < sacarDinheiro:
        print()
        print("Saldo insuficiente.")
    else:
        saldoConta-=sacarDinheiro
        print()
        print("Saque realizado com sucesso!")
        limiteSaque+=1
        listaExtrato.append(f" - Saque: R${sacarDinheiro}")
    return saldoConta,limiteSaque

def verExtrato(listaExtrato,saldoConta):
    if not listaExtrato:
        print()
        print("Sem movimentações!")
        print()
        print(f"Saldo atual: R${saldoConta}")
    else:
        for extrato in listaExtrato:
            print()
            print(extrato)
        print()
        print(f"Saldo atual: R${saldoConta}")

def cadastro(listaClientes):
    cpfCliente=input("Digite seu CPF: ")
    for cliente in listaClientes:
        if cliente["cpf"]==cpfCliente:
            print("CPF já cadastrado!")
            return
    nomeCliente=input("Digite seu nome: ")
    try:
        idadeCliente=int(input("Digite sua idade: "))
    except ValueError:
        print("Digite apenas números!")
        return
    cliente={
        "nome":nomeCliente,
        "cpf":cpfCliente,
        "idade":idadeCliente
    }
    listaClientes.append(cliente)
    print()
    print("Cliente cadastrado com sucesso!")
def listarClientes(listaClientes):
    if not listaClientes:
        print()
        print("Nenhum cliente cadastrado!")
        print()
    else:
        print()
        print(" CLIENTES: ")
        print()
        for cliente in listaClientes:
            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Idade: {cliente['idade']}")
            print("-"*20)

def menu():
      print(
'''
    SISTEMA BANCÁRIO:
    
    1. Depositar
    2. Sacar
    3. Ver Extrato
    4. Cadastro
    5. Listar Clientes
    6. Sair
'''
)