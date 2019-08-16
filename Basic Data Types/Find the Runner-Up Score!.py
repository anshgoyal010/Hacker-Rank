if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m=max(arr)
    while max(arr)==m:
        arr.remove(m)
    print(max(arr))        
