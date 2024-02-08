"""Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números."""


def calculate():
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    operation = int(input("Escolha uma operação: "))
    if operation not in [1, 2, 3, 4]:
        raise ValueError("Operação inválida")
    try:
        x = int(input("Escolha o primeiro número: "))
        y = int(input("Escolha o segundo número: "))

        match operation:
            case 1:
                print(f"{x} + {y} = {x + y}")
            case 2:
                print(f"{x} - {y} = {x - y}")
            case 3:
                print(f"{x} * {y} = {x * y}")
            case 4:
                print(f"{x} / {y} = {x / y}")
    except ValueError:
        print("Input inválido")


if __name__ == "__main__":
    calculate()
