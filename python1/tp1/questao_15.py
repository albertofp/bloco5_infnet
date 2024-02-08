"""Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas."""

import time


def apresentar_escolhas():
    print("Você está em uma encruzilhada na floresta.")
    time.sleep(1)
    print("Você pode escolher entre dois caminhos:")
    time.sleep(1)
    print("1. Seguir o caminho à esquerda.")
    print("2. Seguir o caminho à direita.")


def escolher_caminho():
    while True:
        escolha = input("Qual caminho você escolhe? (Digite 1 ou 2): ")
        if escolha == "1":
            return "esquerda"
        elif escolha == "2":
            return "direita"
        else:
            print("Opção inválida. Por favor, escolha novamente.")


def resultado_escolha(caminho):
    if caminho == "esquerda":
        print("Você escolheu o caminho à esquerda.")
        time.sleep(1)
        print("Você encontra uma cabana abandonada.")
    elif caminho == "direita":
        print("Você escolheu o caminho à direita.")
        time.sleep(1)
        print("Você se depara com uma ponte sobre um rio.")
    else:
        print("Algo deu errado. Você não escolheu nenhum caminho válido.")


def main():
    apresentar_escolhas()
    caminho_escolhido = escolher_caminho()
    resultado_escolha(caminho_escolhido)


if __name__ == "__main__":
    main()
