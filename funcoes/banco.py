from funcoes.utils import clear

import re

saldo = 0
limite = 500
valor = extratoTxt = ""
numero_saques = 0
LIMITE_SAQUES = 3
EXTRATO_ARQUIVO = "extrato.txt"
VOLTAR = "V"


def saque() -> None:
    valor = recebe_input("Informe o valor do saque:")

    if valor != VOLTAR:
        save(valor, prefix="S")
        print("Saque realizado.")


def deposito() -> None:
    valor = recebe_input("Informe o valor do depósito:")

    if valor != VOLTAR:
        save(valor)
        print("Deposito realizado.")


def extrato() -> None:
    print("extrato exibido.")


def recebe_input(texto: str) -> str:
    REGEX = r"\d+(?:\.\d+)?(?:,\d+)?|[Vv]"

    while True:
        valor = input(texto)
        has_only_digits = re.match(REGEX, valor)

        if has_only_digits:
            valor = has_only_digits.group()

            if valor == "v":
                return VOLTAR  # caso "v", retorna "V".

            return valor

        clear()
        print("Valor inválido.")
        print('Por favor, informe apenas números. Ex.: "1", "1.00" ou "1,00"\n')
        print('===\nOu informe "v" para voltar.\n')


def limpar_extrato() -> None:
    with open(EXTRATO_ARQUIVO, "w") as history:
        history.write("")


def save(value: str, prefix: str = "D") -> None:

    prefix = "+" if prefix == "D" else "-"

    with open(EXTRATO_ARQUIVO, "a") as history:
        history.write(prefix + value + ";")
