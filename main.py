from recursos.funcoes import depositar,saque,verExtrato,cadastro,listarClientes,menu
saldoConta=0
listaExtrato=[]
limiteSaque=0
listaClientes=[]
while True:
    menu()
    try:
      opcaoUsuario=int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue
    match opcaoUsuario:
        case 1:
            saldoConta=depositar(saldoConta,listaExtrato)
        case 2:
            saldoConta,limiteSaque=saque(saldoConta,limiteSaque,listaExtrato)
        case 3:
            verExtrato(listaExtrato,saldoConta)
        case 4:
            cadastro(listaClientes)
        case 5:
            listarClientes(listaClientes)
        case 6:
            break
        case _:
            print("""
Opção inválida!
    """)
        