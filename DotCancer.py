
def CheckBox(hl,vl,p,r,c,ori):
    n = len(hl)
    if ori == 'h':
        if r-1>=0 and r+1<n:
            if hl[r-1][c] != '___' and vl[r-1][c] != '|' and vl[r-1][c+1] != '|' and hl[r+1][c] != '___' and vl[r][c] != '|' and vl[r][c+1] != '|':
                return 2
            if hl[r-1][c] != '___' and vl[r-1][c] != '|' and vl[r-1][c+1] != '|':
                return True
            if hl[r+1][c] != '___' and vl[r][c] != '|' and vl[r][c+1] != '|':
                return True
        elif r-1>=0 and r+1>=n:
            if hl[r-1][c] != '___' and vl[r-1][c] != '|' and vl[r-1][c+1] != '|':
                return True
        else:
            if hl[r+1][c] != '___' and vl[r][c] != '|' and vl[r][c+1] != '|':
                return True
    if ori == 'v':
        if c-1>=0 and c+1<n:
            if vl[r][c-1] != '|' and hl[r][c-1] != '___' and hl[r+1][c-1] != '___' and vl[r][c+1] != '|' and hl[r][c] != '___' and hl[r+1][c] != '___':
                return 2
            if vl[r][c-1] != '|' and hl[r][c-1] != '___' and hl[r+1][c-1] != '___':
                return True
            if vl[r][c+1] != '|' and hl[r][c] != '___' and hl[r+1][c] != '___':
                return True
        elif c-1>=0 and c+1>=n:
            if vl[r][c-1] != '|' and hl[r][c-1] != '___' and hl[r+1][c-1] != '___':
                return True
        else:
            if vl[r][c+1] != '|' and hl[r][c] != '___' and hl[r+1][c] != '___':
                return True
            
    return False
    
def CheckBoxPrint(hl,vl,r,c):
    if c+1 < n:
        if vl[r][c+1] != '|' and hl[r][c] != '___' and hl[r+1][c] != '___':
            return True
    return False
        
hl = [['___','___'],['___',0],['___',0]]
vl = [['|','|','|'],['|',0,0]]
print(CheckBox(hl,vl,0,1,1,'v'))

def GameOver(hl,vl):
    for i in range(len(hl)):
        for j in range(len(hl[i])):
            if hl[i][j] == '___':
                return False
    for i in range(len(vl)):
        for j in range(len(vl[i])):
            if vl[i][j] == '|':
                return False
    return True



print("Welcome to the game! Please choose what you want to do:")
print()
print("1.Decide the size of the board")
print("2.Start the game")
print("3.Give up and start a new game")
print("4.Exit")
print()
command=int(input("Enter what you want to do: "))
while(command!=4):
    if(command==1):
        n=int(input("Enter the size you want to play on: "))
        hl = [['___' for i in range(n-1)] for j in range(n)]
        vl = [['|' for i in range(n)] for j in range(n-1)]
        hc = 1
        vc = 1
        print('The board looks like:')
        for i in range(n):
            for j in range(n-1):
                print('.',hl[i][j],hc,'_'*(4-len(str(hc))),end='',sep = '')
                hc+=1
            print('.')
            if i != n-1:
                for k in range(n):
                    print(vl[i][k],end='       ')
                print()
                for k in range(n):
                    print(vc,' '*(7-len(str(vc))),end = '')
                    vc+=1
                print()
                for k in range(n):
                    print(vl[i][k],end='       ')
                print()



    elif(command==2):
        print()
        print('Welcome to a new game!')
        print()
        print('''
Reference Board:
.___1___.___2___.___3___.       
|       |       |       |       
1       2       3       4       
|       |       |       |       
.___4___.___5___.___6___.       
|       |       |       |       
5       6       7       8       
|       |       |       |       
.___7___.___8___.___9___.       
|       |       |       |
9      10      11      12
|       |       |       |
.___10__.___11__.___12__.

Input Format:
1)The first letter of the input should contain the orientation of the line (Horizontal/Vertical)
  This is represented by the letter 'h' for Horizontal and 'v' for Vertical.
2)The Second part of the input represents the number index of th line. Look at the reference Image given
  You will notice that there are numbers representing each line of the matrix. 
When it is your turn, enter the numbers in the above format.
For example:
h1, v30, h23 etc.
''')
        p0c = 0
        p1c = 0
        while GameOver(hl,vl) == False:
            player=input("player 1 enter your move: ")
            rows=0
            columns=0
            if(player[0].lower() == 'h'):
                x = int(player[1:])
                co = 1
                for i in range(len(hl)):
                    for j in range(len(hl[i])):
                        if co == x:
                            r = i
                            c = j
                        co+=1
                hl[r][c] = 0

            elif(player[0].lower() == 'v'):
                x = int(player[1:])
                co = 1
                for i in range(len(vl)):
                    for j in range(len(vl[i])):
                        if co == x:
                            r = i
                            c = j
                        co+=1
                vl[r][c] = 0
            
            for i in range(n):
                    print('.',end = '')
                    for j in range(len(hl[i])):
                        if(hl[i][j] != '___'):
                            print('___',end = '.')
                        else:
                            print(' '*3,end = '.')
                    print(' ')
                    if(i != (n-1)):
                        for k in range(len(vl[i])):
                            if(vl[i][k] != '|'):
                                print('|',end='   ')
                            else:
                                print(' '*3,end = ' ')
                        print()
            if CheckBox(hl,vl,0,r,c,player[0].lower()) == True or CheckBox(hl,vl,0,r,c,player[0].lower()) == 2:
                if CheckBox(hl,vl,0,r,c,player[0].lower()) == True:
                    p0c+=1
                else:
                    p0c+=2
                while (CheckBox(hl,vl,0,r,c,player[0].lower()) == True or CheckBox(hl,vl,0,r,c,player[0].lower()) == 2) == True and GameOver(hl,vl)!=True:
                    player=input("player 1 enter your move again: ")
                    rows=0
                    columns=0
                    if(player[0].lower() == 'h'):
                        x = int(player[1:])
                        co = 1
                        for i in range(len(hl)):
                            for j in range(len(hl[i])):
                                if co == x:
                                    r = i
                                    c = j
                                co+=1
                        hl[r][c] = 0

                    elif(player[0].lower() == 'v'):
                        x = int(player[1:])
                        co = 1
                        for i in range(len(vl)):
                            for j in range(len(vl[i])):
                                if co == x:
                                    r = i
                                    c = j
                                co+=1
                        vl[r][c] = 0
                    
                    for i in range(n):
                            print('.',end = '')
                            for j in range(len(hl[i])):
                                if(hl[i][j] != '___'):
                                    print('___',end = '.')
                                else:
                                    print(' '*3,end = '.')
                            print(' ')
                            if(i != (n-1)):
                                for k in range(len(vl[i])):
                                    if(vl[i][k] != '|'):
                                        print('|',end='   ')
                                    else:
                                        print(' '*3,end = ' ')
                                print()
                    if CheckBox(hl,vl,0,r,c,player[0].lower()) == True or CheckBox(hl,vl,0,r,c,player[0].lower()) == 2:
                        if CheckBox(hl,vl,0,r,c,player[0].lower()) == True:
                            p0c+=1
                        else:
                            p0c+=2
            if GameOver(hl,vl) == True:
                break
            player=input("player 2 enter your move: ")
            rows=0
            columns=0
            if(player[0].lower() == 'h'):
                x = int(player[1:])
                co = 1
                for i in range(len(hl)):
                    for j in range(len(hl[i])):
                        if co == x:
                            r = i
                            c = j
                        co+=1
                hl[r][c] = 1
                
            elif(player[0].lower() == 'v'):
                x = int(player[1:])
                co = 1
                for i in range(len(vl)):
                    for j in range(len(vl[i])):
                        if co == x:
                            r = i
                            c = j
                        co+=1
                vl[r][c] = 1
            for i in range(n):
                    print('.',end = '')
                    for j in range(len(hl[i])):
                        if(hl[i][j] != '___'):
                            print('___',end = '.')
                        else:
                            print(' '*3,end = '.')
                    print(' ')
                    if(i != (n-1)):
                        for k in range(len(vl[i])):
                            if(vl[i][k] != '|'):
                                if CheckBoxPrint(hl,vl,i,k) == True:
                                    print('|',end='    ')
                                else:
                                    print('|',end='   ')
                            else:
                                print(' '*3,end = ' ')
                        print()
            if CheckBox(hl,vl,1,r,c,player[0].lower()) == True or CheckBox(hl,vl,1,r,c,player[0].lower()) == 2:
                if CheckBox(hl,vl,1,r,c,player[0].lower()) == True:
                    p1c+=1
                else:
                    p1c+=2
                while (CheckBox(hl,vl,0,r,c,player[0].lower()) == True or CheckBox(hl,vl,1,r,c,player[0].lower()) == 2) and GameOver(hl,vl)!=True:
                    player=input("player 2 enter your move again: ")
                    rows=0
                    columns=0
                    if(player[0].lower() == 'h'):
                        x = int(player[1:])
                        co = 1
                        for i in range(len(hl)):
                            for j in range(len(hl[i])):
                                if co == x:
                                    r = i
                                    c = j
                                co+=1
                        hl[r][c] = 1
                        
                    elif(player[0].lower() == 'v'):
                        x = int(player[1:])
                        co = 1
                        for i in range(len(vl)):
                            for j in range(len(vl[i])):
                                if co == x:
                                    r = i
                                    c = j
                                co+=1
                        vl[r][c] = 1
                    for i in range(n):
                            print('.',end = '')
                            for j in range(len(hl[i])):
                                if(hl[i][j] != '___'):
                                    print('___',end = '.')
                                else:
                                    print(' '*3,end = '.')
                            print(' ')
                            if(i != (n-1)):
                                for k in range(len(vl[i])):
                                    if(vl[i][k] != '|'):
                                        print('|',end='   ')
                                    else:
                                        print(' '*3,end = ' ')
                                print()
                    if CheckBox(hl,vl,1,r,c,player[0].lower()) == True or CheckBox(hl,vl,1,r,c,player[0].lower()) == 2:
                        if CheckBox(hl,vl,1,r,c,player[0].lower()) == True:
                            p1c+=1
                        else:
                            p1c+=2
        if p0c>p1c:
            print('Player 1 won!')   
        else:
            print('Player 2 won!')
        print('Player 1 score:',p0c)
        print('Player 2 score:',p1c)

        


    elif(command==3):
        print("Welcome to the game! Please choose what you want to do:")
        print("1.Decide the size of the board")
        print("2.Place a line")
        print("3.Give up and start a new game")
        print("4.Exit")


    elif(command==4):
        break


    command=int(input("Enter what you want to do: "))


