from itertools import combinations
a=input().split()
a[0]=sorted(list(a[0]))
for i in range(0,int(a[1])):
    l=list(combinations(a[0],(i+1)))
    for j in range(0,len(l)):
        print(*l[j],sep="")
