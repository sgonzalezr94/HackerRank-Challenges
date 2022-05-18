def multiples3and5(limit):
    return sum([i for i in range(1, limit) if any([i % 3 == 0, i % 5 == 0])])


TEST = 10
print(multiples3and5(10))
