def print_rangoli(size):
    for i in range (size,0,-1):
        for j in range(1,i):
            print("-",end="-")
        for k in range(size,i,-1):
            print(chr(97+k-1),end="-")
        for l in range((i-1),size):
            if chr(97+l)!=chr(96+size):
                print(chr(97+l),end="-")
            else:
                print(chr(96+size),end="")
        for m in range(1,i):
            print("-",end="-")
        print()
    for i in range(1,size):
        for j in range(0,i):
            print("-",end="-")
        for k in range(size,(i+1),-1):
            print(chr(97+k-1),end="-")
        for l in range(i,size):
            if chr(97+l)!=chr(96+size):
                print(chr(97+l),end="-") 
            else:
                print(chr(96+size),end="") 
        for m in range(0,i):
            print("-",end="-")              
        print()
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
