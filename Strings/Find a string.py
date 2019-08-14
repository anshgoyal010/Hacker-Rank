def count_substring(a,b):
    l=len(b)
    c=0
    for i in range(0,len(a)-l+1):
        if a[i:i+l]==b:
            c+=1 
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
