TEST_ARRAY = [3, 7, 1, 2, 8, 4, 5]


def missingnumber(numbers_array):
    n = len(numbers_array) + 1
    return (n * (n + 1) // 2) - sum(numbers_array)


print(missingnumber(TEST_ARRAY))
