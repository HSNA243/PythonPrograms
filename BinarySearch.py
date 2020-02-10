import math


def bs(v, l, g,  x):
    m = (l + g) // 2
    if l > len(v)-1:
        return -1
    if g >= 0:
        if x == v[m]:
            return m 
        elif x < v[m]:
            return bs(v,l,m-1,x)
        else :
            return bs(v,m+1,g,x)



print("Enter the array : ")
a = [int(i) for i in input().split()]
print("Enter the number : ")
x = int(input())
ans = bs(a,0,len(a)-1,x)
if ans == -1:
    print("It is not present")
else:
    print("It is present at index",ans)
