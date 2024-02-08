# Recebe dois nomes de usuário e combina os dois de maneira criativa
def combine_usernames(nome1, nome2):
    combined_name = nome1[:len(nome1) // 2] + nome2[len(nome2) // 2:]
    print(f"{nome1} + {nome2} = {combined_name}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
        description=
        "Recebe dois nomes de usuário e combina os dois de maneira criativa")
    parser.add_argument("nome1", help="Primeiro nome", type=str)
    parser.add_argument("nome2", help="Segundo nome", type=str)

    args = parser.parse_args()
    combine_usernames(args.nome1, args.nome2)
