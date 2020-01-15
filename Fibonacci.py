n = int(input("Enter the number: "))

def dpsol():
    fib = [-1] * n

    fib[0] = 0
    fib[1] = 1

    for i in range(2,n):
        fib[i] = fib[i-1] + fib[i-2]

    return fib

def recsol(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recsol(n-1) + recsol(n-2)
    
print("DP solution : ",dpsol())

fib = []
for i in range(n):
    fib.append(recsol(i))
print("Recursive solution : ",fib)