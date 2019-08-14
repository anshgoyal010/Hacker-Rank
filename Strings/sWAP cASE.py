def swap_case(s):
    ns=''
    for i in range(0,len(s)):
        if (s[i].islower())==True:
            ns+=s[i].upper()
        elif (s[i].isupper())==True:
            ns+=s[i].lower()
        else:
            ns+=s[i]        
    return ns

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
