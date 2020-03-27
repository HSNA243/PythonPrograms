from collections import defaultdict

d = defaultdict(list)

def addedge(x,y):
    d[x].append(y)

def dfs(d):
    v = len(d)
    visits = [False]*v
    for i in range(v):
        if visits[i] == False:
            dfsRec(i,visits)

def dfsRec(i,visits):
    visits[i] = True
    print(i,"is visited")
    for j in d[i]:
        if visits[j] == False:
            dfsRec(j,visits)


addedge(0, 2) 
addedge(1, 2) 
addedge(1, 3) 
addedge(1, 4) 
addedge(2, 0) 
addedge(2, 1)
addedge(2, 3) 
addedge(3, 1)
addedge(3, 2)
addedge(4, 1) 

dfs(d)
