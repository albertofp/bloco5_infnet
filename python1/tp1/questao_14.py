"""Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção."""


def votar():
    print("Escolha uma das opções:")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")

    opt1, opt2, opt3 = 0, 0, 0

    opcao = int(input("Voto: "))

    if opcao == 1:
        print("Opção 1 votada: ")
        opt1 += 1
    elif opcao == 2:
        print("Opção 2 votada: ")
        opt2 += 1
    elif opcao == 3:
        print("Opção 3 votada: ")
        opt3 += 1
    else:
        print("Opção inválida")

    print(f"Opção 1: {opt1}")
    print(f"Opção 2: {opt2}")
    print(f"Opção 3: {opt3}")


if __name__ == "__main__":
    votar()
