import numpy as np


def convert_minutes_to_hours(minutes: int) -> None:
    hours = minutes / 60
    print(f"{minutes} minutos = {hours} horas")


def convert_hours_and_minutes_to_minutes(hours: int, minutes: int) -> None:
    total_minutes = (hours * 60) + minutes
    print(f"{hours} horas e {minutes} minutos = {total_minutes} minutos")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
        description=
        "Converte minutos em horas e minutos, e [horas e minutos] em minutos")
    parser.add_argument("minutos", help="Minutos", type=int)
    parser.add_argument("horas", help="Horas", type=int)
    parser.add_argument("horas_minutos", help="Minutos restantes", type=int)

    args = parser.parse_args()

    convert_minutes_to_hours(args.minutos)
    convert_hours_and_minutes_to_minutes(args.horas, args.horas_minutos)
