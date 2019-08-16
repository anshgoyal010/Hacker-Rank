if __name__ == '__main__':
    arr=[]
    n=int(input())
if n>=2 and n<=5:    
    for i in range(n):
        name = input()
        score = float(input())
        arr.append([])
        arr[i].append(name)
        arr[i].append(score)        
a=min(arr,key=lambda x:x[1])
b=min(arr,key=lambda x:x[1])
while b[1]==a[1]:
    arr.remove(min(arr,key=lambda x:x[1]))
    b=min(arr,key=lambda x:x[1])
ar=[]
a=min(arr,key=lambda x:x[1])
arr=sorted(arr)
for i in range(0,len(arr)):    
    if arr[i][1]==a[1]:
        print(arr[i][0])
