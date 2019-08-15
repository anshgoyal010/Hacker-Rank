n,m=input().split()
ar=input().split()
a=set(input().split())
b=set(input().split())
c=0
for i in ar:
    if i in a:
        c+=1
    if i in b:
        c-=1     
print(c)

