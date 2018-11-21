board=[['1','2','3']
,['4','5','6']
,['7','8','9']]
userX='X'
userO='O'
print( board[0])   
print( board[1])   
print( board[2])
turn=1
x=0
while x<9:
    if turn%2!=0:
        indexrow=int(input("player 1 turn,please choose row to enter you mark(between 1-3):"))
        indexcol=int(input("player 1 turn,please choose col to enter you mark(between 1-3):"))
        if indexrow < 1 or indexrow>3:
            print("please choose row between 1-3")
            continue
        if indexcol < 1 or indexcol>3:
            print("please choose col between 1-3")
            continue
        
        indexrow=indexrow-1
        indexcol=indexcol-1
        if board[indexrow][indexcol]=='X' or board[indexrow][indexcol]=='O':
            continue
        board[indexrow][indexcol]=userX
        turn=turn + 1
        x=x+1
        print( board[0])   
        print( board[1])   
        print( board[2])
        
    else:
        indexrow=int(input("player 2 turn,please choose row to enter you mark(between 1-3):"))
        indexcol=int(input("player 2 turn,please choose col to enter you mark(between 1-3):"))
        if indexrow < 1 or indexrow>3:
            print("please choose row between 1-3")
            continue
        if indexcol < 1 or indexcol>3:
            print("please choose col between 1-3")
            continue
        indexrow=indexrow-1
        indexcol=indexcol-1
        if board[indexrow][indexcol]=='X' or board[indexrow][indexcol]=='O':
            continue
        board[indexrow][indexcol]=userO
        turn=turn + 1
        x=x+1
        print( board[0])   
        print( board[1])   
        print( board[2])


    
