"""Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc."""


def get_discounted_value(valor_compra, faixas_desconto):
    discount = 0

    for limite, porcentagem in faixas_desconto:
        if valor_compra >= limite:
            discount = porcentagem

    valor_descontado = valor_compra * discount
    valor_final = valor_compra - valor_descontado

    return valor_final


def main():
    try:
        valor_compra = float(input("Digite o valor da compra em R$: "))
        if valor_compra <= 0:
            print(
                "Valor de compra inválido. Por favor, insira um valor positivo."
            )
            return

        faixas_desconto = [(100, 0.10), (200, 0.15), (300, 0.20), (400, 0.25),
                           (500, 0.30), (600, 0.35), (700, 0.40), (800, 0.45),
                           (900, 0.50), (1000, 0.55)]

        valor_final = get_discounted_value(valor_compra, faixas_desconto)
        print(
            f"O valor final da compra, com desconto aplicado, é de R$ {valor_final:.2f}"
        )

    except ValueError:
        print(
            "Valor de compra inválido. Certifique-se de inserir um número válido."
        )


if __name__ == "__main__":
    main()
