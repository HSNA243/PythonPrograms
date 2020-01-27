print("Enter the array that needs to be sorted: ")
a = [int(i) for i in input().split()]
n = len(a)
swaps = 1
while swaps != 0:
    swaps = 0
    for i in range(n):
        if i+1<n :
            if a[i+1] < a[i]:
                swaps+=1
                a[i],a[i+1] = a[i+1],a[i]
print(a)