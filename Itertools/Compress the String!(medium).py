from itertools import groupby
i=str(input())
for k,j in groupby(i):
    print(*[(len(list(j)),int(k))],end=" ")
    
