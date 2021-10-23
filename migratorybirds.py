

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def loadFile(path):
    file = open(path, 'r')
    return map(int, file.read().split(" "))


def migratoryBirds(arr):
    sorted_arr = sorted(arr)
    countDict = dict()
    last_element = sorted_arr[0]
    counter = 0
    for element in sorted_arr:
        if element == last_element:
            counter += 1
        else:
            countDict[last_element] = counter
            last_element = element
            counter = 1
    countDict[last_element] = counter
    return min([key for key in countDict if countDict[key] == max(countDict.values())])
