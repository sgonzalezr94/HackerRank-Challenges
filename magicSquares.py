POSIBLESQUARES = [
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2] 
    ]

testMatrix  = [
    [4, 9, 2],
 [3, 5, 7],
  [8, 1, 5]
  ]

def formingMagicSquare(s):
    mtxArray = sum(s, [])
    costs = 100
    for mgcSquare in POSIBLESQUARES:
        squareCost = sum([abs(mgcSquare[i] - mtxArray[i]) for i in range(9)])
        costs = costs if costs<squareCost else squareCost
    return costs