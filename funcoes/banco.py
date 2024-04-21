saldo = 0
limite = 500
valor = extratoTxt = ""
numero_saques = 0
LIMITE_SAQUES = 3
EXTRATO_ARQUIVO = "extrato.txt"


def saque() -> None:
    valor = input("Informe o valor do saque:")
    save(valor, prefix="S")
    print("saque realizado.")


def deposito() -> None:
    valor = input("Informe o valor do depósito:")
    save(valor)
    print("deposito realizado.")


def extrato() -> None:
    print("extrato exibido.")


def limpar_extrato() -> None:
    with open(EXTRATO_ARQUIVO, "w") as history:
        history.write("")


def save(value: str, prefix: str = "D") -> None:

    prefix = "+" if prefix == "D" else "-"

    with open(EXTRATO_ARQUIVO, "a") as history:
        history.write(prefix + value + ";")
