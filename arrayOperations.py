
# Starting with a 1-indexed array of zeros and a list of operations,
#  for each operation add a value to each the array element between two given indices, inclusive.
#   Once all operations have been performed, return the maximum value in the array.


from itertools import accumulate

TST_ARRAY = [[1,2,100],[2,5,100],[3,4,100]]

def openTestCase(path):
    doc = open(path,'r').readlines()
    newdoc = map( lambda line: list(map(int,line.replace('/n','').split(" "))),doc)
    return list(newdoc)[1:]

def arrayManipulation(n, queries):
    array = [0]*n
    for query in queries:
        array[query[0]-1] += query[2]
        if query[1]<n:
            array[query[1]] -= query[2]
    return max(accumulate(array))


hr_test = openTestCase('testCase.txt')
print(hr_test)
mau = arrayManipulation(10000000,hr_test)
print(mau)