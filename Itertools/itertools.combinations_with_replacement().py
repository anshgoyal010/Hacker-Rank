from itertools import combinations_with_replacement
a=input().split()
a[0]=sorted(list(a[0]))
l=list(combinations_with_replacement(a[0],int(a[1])))
for j in range(0,len(l)):
    print(*l[j],sep="")

