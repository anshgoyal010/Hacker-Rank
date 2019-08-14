def minion_game(s):
    l=len(s)
    a=0
    b=0
    for i in range(0,l):
        if s[i]!='A' and s[i]!='E' and s[i]!='I' and s[i]!='O' and s[i]!='U':
            a+=(l-i)
        else:
            b+=(l-i)
    if a>b:
        print("Stuart",end=" ")
        print(a)
    elif b>a:
        print("Kevin",end=" ")
        print(b)
    else:
        print("Draw")                     

if __name__ == '__main__':
    s = input()
    minion_game(s)
