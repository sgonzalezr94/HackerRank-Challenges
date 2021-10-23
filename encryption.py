
import math 
from itertools import zip_longest
S = "if man was meant to stay on the ground god would have given us roots"
S1 = "chillout"

def encryption(s):
    s = s.replace(' ','')
    l = len(s)
    rows = math.floor(math.sqrt(l))
    columns = math.ceil(math.sqrt(l))
    if rows*columns>=l:
        mtx = [list(s[idx : idx + columns]) for idx in range(0,l,columns)]
    else:
        mtx = [list(s[idx : idx + columns]) for idx in range(0,l,max(rows,columns))]
    zipped = zip_longest(*mtx,fillvalue='')
    finalstr = " ".join(map("".join,list(zipped)))
    return finalstr
       


print(encryption(S1))
