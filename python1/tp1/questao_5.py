"""Crie um programa que peça ao usuário seu nome e sobrenome usando input e, em seguida, combine-os para formar uma saudação personalizada."""


def hello():
    try:
        name = str(input("Qual seu nome? "))
        surname = str(input("Qual seu sobrenome? "))
        print(f"Ola, {name} {surname}!")
    except ValueError:
        print("Input inválido")


if __name__ == "__main__":
    hello()
