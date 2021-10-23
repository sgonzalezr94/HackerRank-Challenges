

def staircase(n):
    outstr = [" "]*n
    for i in range(0, n):
        outstr[-(i+1)] = "#"
        print("".join(outstr))
