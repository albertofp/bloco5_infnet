import random
"""Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo."""


def guess_number():
    number = random.randint(1, 1000)
    guess = int(input("Adivinhe o número: "))
    while guess != number:
        match guess:
            case guess if guess > number:
                print("Muito alto")
            case guess if guess < number:
                print("Muito baixo")
        guess = int(input("Tente novamente: "))
    print(f"Acertou! O número era {number}")
    return


if __name__ == "__main__":
    guess_number()
