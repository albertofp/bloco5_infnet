import numpy as np


def process_numbers(x: np.double, y: np.double) -> None:
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
        description=
        "Recebe dois números e calcula o resultado das 4 operações aritmeticas: adição, subtração, divisão e multiplicação"
    )
    parser.add_argument("x", help="Primeiro valor", type=np.double)
    parser.add_argument("y", help="Segundo valor", type=np.double)

    args = parser.parse_args()

    process_numbers(args.x, args.y)
