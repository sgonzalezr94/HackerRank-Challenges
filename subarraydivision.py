

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

# Sebastian Gonzalez - 8/2/2021
# There's something regarding the array, if it was sorted the task could potentially be solved in O(n)
# Need to take a look into hashing tho


def birthday(s, d, m):
    nways = 0
    initialidx = 0
    while(initialidx+m <= len(s)):
        if sum(s[initialidx:initialidx+m]) == d:
            nways += 1
        initialidx += 1
    print(nways)
    return nways
