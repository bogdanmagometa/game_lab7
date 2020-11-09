"""
numbers_generator.py

This module is used for generating lists of numbers such as Ulam numbers, lucky
numbers and even numbers.

It consists of 3 function:
gen_ulam(length)
gen_lucky(length)
gen_even(length)
"""

from typing import List


def gen_ulam(length: int) -> List[int]:
    """
    Precondition: n > 0

    Returns sequence of n Ulam numbers.

    >>> gen_ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> gen_ulam(54) # doctest: +NORMALIZE_WHITESPACE
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69,
    72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138, 145, 148, 155, 175,
    177, 180, 182, 189, 197, 206, 209, 219, 221, 236, 238, 241, 243, 253, 258,
    260, 273, 282]
    >>> gen_ulam(2)
    [1, 2]
    >>> gen_ulam(1)
    [1]
    >>> gen_ulam(3)
    [1, 2, 3]
    """

    if length == 1:
        return [1]
    if length == 2:
        return [1, 2]

    sequence = [1, 2]

    # find another n-2 Ulam numbers
    for _ in range(length - 2):
        candidates_for_ulam = []
        repeating_numbers = []

        # go through all the combinations of two numbers (num1 and num2) from sequence
        for index_num1, num1 in enumerate(sequence):
            for num2 in sequence[index_num1+1:]:

                candidate = num1 + num2

                if candidate > sequence[-1]:
                    if candidate in candidates_for_ulam:
                        candidates_for_ulam.remove(candidate)
                        repeating_numbers.append(candidate)
                    elif candidate not in repeating_numbers:
                        candidates_for_ulam.append(candidate)

        sequence.append(min(candidates_for_ulam))

    return sequence


def gen_lucky(length: int) -> List[int]: ## need to rewrite but works fine
    """
    Precondition: 0 <= n <= 1200

    Generates and returns list of n lucky numbers.

    >>> gen_lucky(100) # doctest: +ELLIPSIS
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, ... 75, 79, 87, 93, 99, ...]
    >>> gen_lucky(4)
    [1, 3, 7, 9]
    >>> gen_lucky(0)
    []
    >>> gen_lucky(1)
    [1]
    >>> gen_lucky(2)
    [1, 3]
    >>> gen_lucky(3)
    [1, 3, 7]
    >>> gen_lucky(1200) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, ..., 9999, ...]
    >>> gen_lucky(3)
    [1, 3, 7]
    """

    natur_list = list(range(1, 11_000))

    cur_num = 2
    i = length
    while i > 0:
        if cur_num in natur_list:
            del natur_list[cur_num-1::cur_num]
            i -= 1
        cur_num += 1

    return natur_list[:length]


def gen_even(length: int) -> List[int]:
    """
    Precondition: n > 0

    Returns list containing n even numbers starting from 2

    >>> gen_even(1)
    [2]
    >>> gen_even(2)
    [2, 4]
    >>> gen_even(3)
    [2, 4, 6]
    >>> gen_even(4)
    [2, 4, 6, 8]
    >>> gen_even(10_000) # doctest: +ELLIPSIS
    [2, 4, 6, 8, 10, ..., 9998, 10000, 10002, ..., 19996, 19998, 20000]
    """

    return list(range(2, 2*length + 1, 2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
