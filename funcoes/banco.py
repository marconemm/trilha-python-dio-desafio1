from funcoes.utils import clear

import re

saldo = 0.0
limite = 500.00
extratoTxt = ""
numero_saques = 0
LIMITE_SAQUES = 3
EXTRATO_ARQUIVO = "extrato.txt"
VOLTAR = "V"


def saque() -> None:
    global saldo, limite, numero_saques, LIMITE_SAQUES, VOLTAR
    ERR_TXT = "Saque não realizado."
    VALOR = recebe_input("Informe o valor do saque:")

    if VALOR != VOLTAR:
        if VALOR <= saldo:
            saldo -= VALOR
            save(VALOR, prefix="S")
            atualiza_extrato()

            numero_saques += 1
            print("Saque realizado.")

        elif numero_saques > LIMITE_SAQUES:
            print("Você já atingiu o limite de saques diários.")
            print(ERR_TXT)

        else:
            txtSaldo = str(saldo).replace(".", ",")

            print(f"O saldo atual é insuficiente: R$ {txtSaldo}.")
            print(ERR_TXT)


def deposito() -> None:
    valor = recebe_input("Informe o valor do depósito:")

    if valor != VOLTAR:
        save(valor)
        print("Deposito realizado.")


def extrato() -> None:
    print("extrato exibido.")


def recebe_input(texto: str) -> str | float:
    REGEX = r"\d+(?:\.\d+)?(?:,\d+)?|[Vv]"

    while True:
        valor = input(texto)
        has_only_digits = re.match(REGEX, valor)

        if has_only_digits:
            valor = has_only_digits.group()

            if valor == "v" or valor == "V":
                return VOLTAR  # sempre retorna "V".

            return converte_valor(valor)  # sempre retorna um valor no padrão X.XX

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


def converte_valor(valor: str) -> float:
    valor = valor.replace(",", ".")

    return float(valor)


def atualiza_extrato() -> str:
    with open(EXTRATO_ARQUIVO, "r") as history:
        extratoTxt = ""
        line = history.readline().split(";")

        for value in line:
            value = float(value)

            if value > 0:
                extratoTxt += f"DEPOSITO ===== > R${value}C\n"
            else:
                extratoTxt += f"SAQUE ======== > R${value}D\n"

    extratoTxt += f"----\nSALDO ======== > R${saldo}C\n----\n"
