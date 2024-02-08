import random
"""Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados."""


def randomize_dice(number_of_dice: int):
    for i in range(number_of_dice):
        dice = random.randint(1, 6)
        print(f"Dado {i + 1}: {dice}")


if __name__ == "__main__":
    number_of_dice = int(input("Quantos dados deseja jogar? "))
    randomize_dice(number_of_dice)
