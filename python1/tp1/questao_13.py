"""Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente)."""


def verificar_palindromo(palavra: str):
    if palavra == palavra[::-1]:
        print("Palíndromo")
    else:
        print("Não é um palíndromo")


if __name__ == "__main__":
    palavra = str(input("Insira uma palavra ou frase: "))
    verificar_palindromo(palavra)
