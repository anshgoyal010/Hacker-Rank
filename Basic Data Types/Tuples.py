if __name__ == '__main__':
    n = int(input())
    int_list =list(map(int, input().split()))
t=(tuple(int_list))
print(hash(t))
