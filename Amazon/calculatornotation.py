# ["8","5","-","7","/"]
# operations -+*/
# positive numbers
# scalable y mantainable
from ast import expr
from typing import List

operations = "+-/*"


class Calculator:
    def __init__(self, operations) -> None:
        self.operations = operations

    def __add(self):
        pass

    def __perform_operation(self, expression):
        expression_stack = list()
        for character in expression:
            if character not in operations:
                expression_stack.append(character)
            elif expression_stack:
                pass


calc = Calculator(operations=operations)
