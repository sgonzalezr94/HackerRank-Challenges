# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

test = [1,3,2,6,1,2]
#If the given list is ordered, that means we can use the init and end of the list, since it isn't we need to check each element with the other ones.
def divisibleSumPairs(n, k, ar):
    pairs = set()
    for fst_idx, fst_element in enumerate(ar):
        for scnd_idx, scnd_element in enumerate(ar):
            if fst_idx!=scnd_idx:
                if (fst_element+scnd_element)%k==0 and (scnd_idx,fst_idx) not in pairs:
                    pairs.add((fst_idx,scnd_idx))
    return len(pairs)



divisibleSumPairs(6,3,test)





