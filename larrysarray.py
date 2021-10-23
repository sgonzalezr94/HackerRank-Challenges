

def larrysArray(A):
    assertsCount = 0
    for idx,currValue in enumerate(A):
        checkList = [nextNum>currValue for nextNum in A[:idx]]
        assertsCount+=sum(checkList)
    if assertsCount%2==0:
       print("YES")
       return "YES"
    else:
        print("NO")
        return "NO"
