from itertools import permutations
a=input().split()
li=(sorted(list(permutations(a[0],int(a[1])))))
for i in range(0,len(li)):
    print(*li[i],sep="")
