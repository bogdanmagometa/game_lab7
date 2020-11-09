"""
field_generator.py

This module works with field of numbers in our game.
It contains functions for generating field as a list
of integers and generating grid as a string for
displaying numbers.
"""

import random


def gen_field(ulam_numbers: list, lucky_numbers: list, even_numbers: list, height: int,
                                                                            length: int) -> list:
    """
    This function takes three lists of Ulam, lucky and even numbers and returns
    a game field as a list

    Precondition: height > 0 and length > 0
    Precondition: (height * length) % 3 == 0
    """
    num_elements = height * length

    field_set = set()

    counter = 0
    while len(field_set) < num_elements:
        if counter % 3 == 0:
            field_set.add(random.choice(ulam_numbers))
        elif counter % 3 == 1:
            field_set.add(random.choice(lucky_numbers))
        else:
            field_set.add(random.choice(even_numbers))
        counter += 1

    field = list(field_set)
    random.shuffle(field)

    return field


def gen_grid(field: list, height: int, width: int) -> str:
    """
    Precondition: len(field) == height*width
    Precondition height > 0 and width > 0

    Returns field as grid with specified height and width.
    Parameter field has to be a list of elements.
    """
    space_per_element = 6

    num_element = 0

    grid = ""

    grid += '\u2015'*(width*(space_per_element+1)+1) + '\n'
    for _ in range(height):
        for _ in range(width):
            grid += "|"

            grid += f"{field[num_element]:^{space_per_element}}"
            num_element += 1
        grid += '|\n'

        grid += '\u2015'*(width*(space_per_element+1)+1) + '\n'

    return grid
