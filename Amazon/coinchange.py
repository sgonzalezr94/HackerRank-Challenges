from typing import List
from math import ceil

DENOMINATIONS = [1, 2, 5]

MONEY = 7


def provide_change_ways(denominations: List[int], money: int) -> dict:
    change_dict = dict()
    for denomination in denominations:
        denomination_string = str(denomination) * (int(money // denomination)) + str(
            (money - ceil((float(money // denomination))))
            * ceil((float(money // denomination)))
            if (float(money // denomination) in denominations)
            else 0
        )
        change_dict[denomination] = denomination_string
    print(change_dict)
    return change_dict


test = provide_change_ways(DENOMINATIONS, MONEY)
