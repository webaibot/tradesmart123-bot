import random


def format_currency(value: float) -> str:
    return f'${value:,.2f}'


def random_choice(options: list) -> str:
    return random.choice(options)