def average(array):
    s=set(arr)
    return (sum(s)/len(s))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
