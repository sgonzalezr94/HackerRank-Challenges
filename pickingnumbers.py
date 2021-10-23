

def pickingNumbers(a):
    maximun = 0
    for integer in a:
        curr_count = a.count(integer)
        prev_count = a.count(integer-1)
        if curr_count+prev_count > maximun:
            maximun = curr_count+prev_count
    print(maximun)
    return maximun
