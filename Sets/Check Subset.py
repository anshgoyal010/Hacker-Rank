T=int(input())
for i in range(0,T):
    n=int(input())
    na=set(map(int,input().split()))
    m=int(input())
    ma=set(map(int,input().split()))
    if (len(ma-na))==(m-n):
        print("True")
    else:
        print("False")
