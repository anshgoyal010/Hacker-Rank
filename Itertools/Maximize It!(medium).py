from itertools import product
K,M=map(int,input().split())
li=[]
for i in range(0,K):
    a=list(map(int,(input().split())))
    a.remove(a[0])
    li.append(a)
la=list(product(*li))
maxi=0 
for i in range(0,len(la)):
    n=0
    for j in (la[i]):
        n+=j*j
    s=n%M
    if s>maxi:
        maxi=s
print(maxi)
