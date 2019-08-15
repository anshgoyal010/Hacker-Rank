n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(0,m):
    ar=input().split()

    if ar[0]=="remove":
        if ar[1] in s:
            s.remove(int(ar[1]))
    if ar[0]=="pop":
        s.pop()
    else:
        s.discard(int(ar[1]))      
print(sum(s))
