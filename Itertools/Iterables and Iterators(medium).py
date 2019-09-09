from itertools import combinations
n=int(input())
l=list(input().split())
k=int(input())
li=list(combinations(l,k))
no=(len(li))
c=0
for i in range(0,no):
    if 'a' in li[i]:
        c+=1
print(c/no)       
