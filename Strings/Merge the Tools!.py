def merge_the_tools(string, k):
    l=len(string)
    for i in range(0,l,k):
        s=(string[i:i+k])
        li=[]
        for j in range(0,k):
            if s[j] not in li:
                li.append(s[j])
        print(*li,sep="")


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
