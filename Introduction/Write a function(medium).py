def is_leap(year):
    leap = False
    if ((year%4)==0) and year>=1900 and year<=100000:
        if ((year%100)!=0):
            leap=True
        elif (((year%100)==0) and ((year%400)==0)):
            leap=True
    return leap

year = int(input())
print(is_leap(year))
