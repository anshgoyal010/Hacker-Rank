n=int(input())
sn=set(map(int,input().split()))
m=int(input())
for i in range(0,m):
    a=input().split()
    b=set(map(int,input().split()))
    if a[0]=="intersection_update":
        sn.intersection_update(b)
    if a[0]=="update":
        sn.update(b)
    if a[0]=="symmetric_difference_update":
        sn.symmetric_difference_update(b)
    if a[0]=="difference_update":
        sn.difference_update(b)
print(sum(sn))
