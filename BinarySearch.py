
import math


def bs(v , x):
    m = math.ceil(len(v)/2) - 1
    if (len(v) == 1):
        if (v[0] == x):
            return "Present"
        else:
            return "Absent"
    else:
        if (x == v[m]):
            return "Present"
        elif (x < v[m]):
            return bs(v[0:m+1],x)
        else :
            return bs(v[m+1:],x)

print("Enter the array : ")
a = [int(i) for i in input().split()]
print("Enter the number : ")
x = int(input())
print(bs(a,x))