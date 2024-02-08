"""Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não."""


def is_adult():
    age = int(input("Qual sua idade? "))
    if age >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")
    return


if __name__ == "__main__":
    is_adult()
