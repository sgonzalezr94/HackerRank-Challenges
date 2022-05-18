# Determine if the sum of two integers is equal to the given value

import re


TEST_ARRAY = [5, 7, 1, 2, 8, 4, 3]
TARGET = 15


def is_sum_in_array(numbers_array: list, target: int) -> bool:
    numbersdict = dict()
    for number in numbers_array:
        if target - number in numbersdict:
            return True
        else:
            numbersdict[number] = 0
    return False


is_sum_in_array(TEST_ARRAY, TARGET)
