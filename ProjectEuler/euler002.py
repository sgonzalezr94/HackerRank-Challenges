# Horrible Complexity, this is O(n!)
# def fibonacci(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# We want to improve this, we should use DP

FIB_DICT = {0: 0, 1: 1, 2: 1}


def fibonacci(n: int) -> int:
    global FIB_DICT
    if n in FIB_DICT:
        return FIB_DICT[n]
    else:
        FIB_DICT[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return FIB_DICT[n]


print(fibonacci(1000))
