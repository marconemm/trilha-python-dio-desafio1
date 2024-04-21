from funcoes.utils import clear
from funcoes.banco import deposito, extrato, saque, limpar_extrato


menu = """
===
Escolha uma das opções a seguir:

1 - Depositar
2 - Sacar
3 - Extrato
4 - Limpar Extrato
0 - Sair

=> """

opcao = ""
OPCOES_VALIDAS = ("0", "1", "2", "3", "4")

while True:
    opcao = input(menu)

    if opcao not in OPCOES_VALIDAS:
        clear()
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    if opcao == "1":
        deposito()

    elif opcao == "2":
        saque()

    elif opcao == "3":
        extrato()

    elif opcao == "4":
        limpar_extrato()

    elif opcao == "0":
        print("\nAté breve! =)\n")
        break
