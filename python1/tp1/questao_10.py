"""Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa."""

import random


def gerar_historia(personagens, acoes, locais):
    personagem = random.choice(personagens)
    acao = random.choice(acoes)
    local = random.choice(locais)

    historia = f"{personagem} {acao} {local}."
    return historia


def main():
    personagens = [
        "João", "Maria", "Pedro", "Ana", "Carlos", "Lucas", "Julia", "Marta",
        "Felipe"
    ]
    acoes = [
        "encontrou um tesouro",
        "viajou para o espaço",
        "descobriu um portal mágico",
        "derrotou um dragão",
        "construiu uma máquina do tempo",
        "encontrou uma pedra preciosa",
        "encontrou um tesouro mágico",
        "roubou um navio",
        "derrotou um gigante",
    ]
    locais = [
        "na floresta",
        "em uma cidade abandonada",
        "no fundo do oceano",
        "no topo de uma montanha",
        "em um planeta distante",
        "no mar",
        "no campo de futebol",
        "na montanha",
        "em um castelo",
    ]

    historia = gerar_historia(personagens, acoes, locais)
    print("História gerada:")
    print(historia)


if __name__ == "__main__":
    main()
