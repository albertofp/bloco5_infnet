"""Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais)."""


def classificar_palavras(palavra: str):
    if len(palavra) < 5:
        print("curta")
    else:
        print("longa")


if __name__ == "__main__":
    palavra = str(input("Insira uma palavra: "))
    classificar_palavras(palavra)
