from funcoes.utils import clear

import re

saldo = 0.0
extratoTxt = ""
numero_saques = 0
SAQUE_MAXIMO = 500.00
LIMITE_SAQUES = 3
EXTRATO_ARQUIVO = "extrato.txt"
VOLTAR = "V"


def saque() -> None:
    global saldo, numero_saques, SAQUE_MAXIMO, LIMITE_SAQUES, VOLTAR
    ERR_TXT = "Saque não realizado."
    VALOR = recebe_input("Informe o valor do saque:")

    if VALOR != VOLTAR:
        VALOR_PERMITIDO = VALOR <= SAQUE_MAXIMO
        PODE_SACAR = numero_saques < LIMITE_SAQUES
        TEM_SALDO = VALOR <= saldo

        if not VALOR_PERMITIDO:
            print("O valor máximo por saque é de R$ 500,00")
            print(ERR_TXT)

        elif not PODE_SACAR:
            print("Você já atingiu o limite de saques diários.")
            print(ERR_TXT)

        elif not TEM_SALDO:
            txtSaldo = str(saldo).replace(".", ",")

            print(f"O saldo atual é insuficiente: R$ {txtSaldo}.")
            print(ERR_TXT)

        else:
            saldo -= VALOR
            save(VALOR, prefix="S")
            numero_saques += 1
            print("Saque realizado.")


def deposito() -> None:
    global saldo
    valor = recebe_input("Informe o valor do depósito:")

    if valor != VOLTAR:
        save(valor)
        saldo += valor

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


def save(value: float, prefix: str = "D") -> None:

    with open(EXTRATO_ARQUIVO, "a") as history:
        prefix = "+" if prefix == "D" else "-"
        value = str(value)

        history.write(prefix + value + ";")

    atualiza_extrato()


def converte_valor(valor: str) -> float:
    valor = valor.replace(",", ".")

    return float(valor)


def atualiza_extrato() -> str:
    with open(EXTRATO_ARQUIVO, "r") as history:
        extratoTxt = ""
        line = history.readline().split(";")

        for value in line:
            if value:
                value = float(value)

                if value > 0:
                    extratoTxt += f"DEPOSITO ===== > R${value}C\n"
                else:
                    extratoTxt += f"SAQUE ======== > R${value}D\n"

    extratoTxt += f"----\nSALDO ======== > R${saldo}C\n----\n"
