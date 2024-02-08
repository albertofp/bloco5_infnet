"""Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso)."""


def get_imc():
    weight = float(input("Qual seu peso(kg)? "))
    height = float(input("Qual sua altura(cm)? "))
    imc = round(weight * 10**4 / (height**2), 2)
    print(f"Seu IMC é {imc}")

    match imc:
        case imc if imc < 18.5:
            print("Abaixo do peso")
        case imc if imc >= 18.5 and imc < 25:
            print("Peso normal")
        case imc if imc >= 25 and imc < 30:
            print("Sobrepeso")
        case imc if imc >= 30:
            print("Obeso")


if __name__ == "__main__":
    get_imc()
