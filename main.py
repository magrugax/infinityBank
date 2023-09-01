from banco import *
from operacoes.depostito import depositar
from operacoes.saque import sacar
from operacoes.consulta import consultarSaldo
from operacoes.tranferencia import transferir


def menu():
    while True:
        print("----Sistema Bancário----")
        print("1 - ADICIONAR CONTA")
        print("2 - EDITAR CONTA")
        print("3 - CONSULTAR CONTA")
        print("4 - APAGAR CONTA")
        print("5 - LISTAR CONTAS")
        print("6 - REALIZAR SAQUE")
        print("7 - REALIZAR DEPOSITO")
        print("8 - TRANFERENCIA")
        print("9 - CONSULTA SALDO")
        print("10 - SAIR")

        opcao = int(input("Selecione uma opção:> "))

        if opcao == 1:
            nome = input("Digite o nome do cliente: ")
            saldo = float(input("Digite o saldo: "))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input("Digite o número da conta: "))
            nome = input("Digite o nome do cliente: ")
            editarNome(conta, nome)
        elif opcao == 3:
            conta = int(input("Digite o número da conta: "))
            buscarCliente(conta)
        elif opcao == 4:
            conta = int(input("Digite o número da conta: "))
            removerConta(conta)
        elif opcao == 5:
            listarTodos()
        elif opcao == 6:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do deposito: "))
            depositar(conta, valor)
        elif opcao == 8:
            contaOrigem = int(input("Informe a conta de origem: "))
            contaDestino = int(input("Informe a conta de destino: "))
            valor = float(input("Digite o valor que deseja transferir: "))
            transferir(contaOrigem, contaDestino, valor)
        elif opcao == 9:
            conta = int(input("Digite o número da conta: "))
            consultarSaldo(conta)
        elif opcao == 10:
            print("--- VOCÊ SAIU DO PROGRAMA ---")
            break
        else:
            print("Opção inválida!")

menu()
