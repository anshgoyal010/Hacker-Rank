import textwrap

def wrap(string, max_width):
    c=0
    for i in range(0,len(string)):
        c+=1
        if (c%max_width)==0:
            print(string[i])
        else:
            print(string[i],end="")     
    return "\n"

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
