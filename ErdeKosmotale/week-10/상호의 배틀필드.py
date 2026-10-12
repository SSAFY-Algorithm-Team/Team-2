# 벽돌로 만든 벽은 포탄 맞으면 평지로 바뀜
# 강철로 만든 벽은 포탄 맞으면 아무일도 없어

T = int(input())

for test_case in range(1 , T + 1):

    H , W = map(int,input().split())

    lst = [list(input()) for _ in range(H)]

    N = int(input())

    command = list(input())

    start_row = 0
    start_col = 0 
    direction= ''

    for row in range(H):
        for col in range(W):
            if(lst[row][col] in ['^','v','<','>']):
                start_row = row
                start_col = col
                direction = lst[row][col]

    c_row = start_row
    c_col = start_col

    lst[c_row][c_col] = '.'

    for cmd in command:

        if(cmd == 'U'):
            n_row = c_row - 1
            n_col = c_col
            direction = '^'
            if(n_row < 0 ):
                continue

            if(lst[n_row][c_col]=='.'):
                c_row, c_col = n_row, n_col

            
        elif(cmd == 'D'):
            n_row = c_row +1
            n_col = c_col
            direction = 'v'

            if(n_row >= H):
                continue

            if(lst[n_row][n_col]=='.'):
                c_row, c_col = n_row, n_col

        elif(cmd == 'L'):
            n_row = c_row
            n_col = c_col -1
            direction ='<'
            if(n_col < 0):
                continue

            if(lst[n_row][n_col]=='.'):
                c_row, c_col = n_row, n_col

        elif(cmd == 'R'):
            n_row = c_row
            n_col = c_col + 1
            direction = '>'
            if(n_col >= W):
                continue

            if(lst[n_row][n_col]=='.'):
                c_row, c_col = n_row, n_col

        elif(cmd == 'S'):

            if(direction == '^'):

                for row in range(c_row, -1, -1):

                    if(lst[row][c_col]=='#'):
                        break

                    if(lst[row][c_col]=='*'):
                        lst[row][c_col] = '.'
                        break
            
            elif(direction == 'v'):
            
                for row in range(c_row, H, +1):

                    if(lst[row][c_col]=='#'):
                        break

                    if(lst[row][c_col]=='*'):
                        lst[row][c_col] = '.'
                        break
            
            elif(direction == '<'):
                        
                for col in range(c_col, -1, -1):

                    if(lst[c_row][col]=='#'):
                        break

                    if(lst[c_row][col]=='*'):
                        lst[c_row][col] = '.'
                        break

            elif(direction == '>'):
                                    
                for col in range(c_col, W, +1):

                    if(lst[c_row][col]=='#'):
                        break

                    if(lst[c_row][col]=='*'):
                        lst[c_row][col] = '.'
                        break

    lst[c_row][c_col]= direction


    print(f"#{test_case}",end=' ')
    for i in range(H):
        print(''.join(lst[i]))
                        
    