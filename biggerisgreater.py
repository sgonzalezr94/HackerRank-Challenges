

def biggerIsGreater(w):
    w = list(w)
    idx = len(w)-1

    while(idx > 0 and w[idx-1] >= w[idx]):
        idx -= 1

    if idx <= 0:
        return "no answer"

    idx2 = len(w)-1

    while(w[idx2] <= w[idx-1]):
        idx2 -= 1

    w[idx-1], w[idx2] = w[idx2], w[idx-1]

    w[idx:] = w[len(w)-1:idx-1:-1]

    return "".join(w)
