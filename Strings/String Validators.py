if __name__ == '__main__':
    s = input()
    a=b=c=d=e=0
    for i in range(0,len(s)):
        if s[i].isalnum():
            a=1
        if s[i].isalpha():
            b=1
        if s[i].isdigit():
            c=1
        if s[i].islower():
            d=1
        if s[i].isupper():
            e=1
    if a==1:
        print("True")
    else:
        print("False")
    if b==1:
        print("True")
    else:
        print("False")
    if c==1:
        print("True")
    else:
        print("False")
    if d==1:
        print("True")
    else:
        print("False")
    if e==1:
        print("True")
    else:
        print("False")
