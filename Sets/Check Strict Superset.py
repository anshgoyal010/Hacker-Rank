A=set(map(int,input().split()))
n=int(input())
m=0
for i in range(0,n):
    X=A
    z=set(map(int,input().split()))
    Y=z
    if len(Y-X)==0 and len(X-z)>0:
        m+=1
if m==n:
    print("True")
else:
    print("False")    
