def merge(a , l , r):
    i = 0
    j = 0
    f = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[f] = l[i]
            i+=1
            f+=1
        else:
            a[f] = r[j]
            j+=1
            f+=1
    
    while i < len(l):
        a[f] = l[i]
        i+=1
        f+=1
    
    while j < len(r):
        a[f] = r[j]
        j+=1
        f+=1
    
def mergesort(a):
    if len(a) > 1:
        m = len(a)//2
        l = a[:m]
        r = a[m:]
        mergesort(l)
        mergesort(r)
        merge(a,l,r)
        return a

print("Enter the array you want to sort:")
a = [int(i) for i in input().split()]
print("the sorted array is:")
print(mergesort(a))