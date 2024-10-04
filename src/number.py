import os
from typing import Iterable

from src.util import print_hello


def sum_even_numbers(numbers: Iterable[int]) -> int:
    print_hello()

    return sum(num for num in numbers if num % 2 == 0)
