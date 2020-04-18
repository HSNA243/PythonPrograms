n = int(input("Enter the number of disks: "))
A = []
B = []
C = []
for k in range(n):
    A.append(n-k)

print(A,B,C)


def toh(n, frm, to, aux):
    if n == 1 :
        print("Move 1 from",frm,"to",to)
        return
    toh(n-1, frm, aux, to)
    print("Move",n,"from",frm,"to",to)
    toh(n-1, aux, to, frm)

def Tower2(n, frm, to, aux):
    if n == 1 :
        to.append(frm.pop())
        print(A,B,C)
        return
    Tower2(n-1, frm, aux, to)
    to.append(frm.pop())
    print(A,B,C)
    Tower2(n-1, aux, to, frm)


Tower2(n, A, C, B)