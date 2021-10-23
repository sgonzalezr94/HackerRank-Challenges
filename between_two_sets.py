

def getTotalX(a, b):
    count = 0
    arr = []
    for num in range(max(a), min(b) + 1, max(a)):
        left = all([num % numA == 0 for numA in a])
        right = all([numB % num == 0 for numB in b])
        if right & left:
            arr.append(num)
    return len(arr)


a = [2, 3]
b = [24, 36]

print(getTotalX(a, b))
