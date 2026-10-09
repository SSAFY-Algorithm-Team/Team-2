# 명령은 문자로 주어짐, 2차원 격자 모양으로 줄지어 있다
# 이동 방향이 상하좌우로 바뀔수가 있음
# 처음 위치는 [0,0]이고 이동 방향은 오른쪽임.
 
from collections import deque

T = int(input())

def bfs():

    visited[(0,0,3,0)]=1

    queue.append((0,0,3,0))

    while(queue):

        row, col, direction, memory = queue.popleft()

        if(lst[row][col]=='@'):
            return 'YES'

        if(lst[row][col]=='<'):
            direction = 2
        elif(lst[row][col]=='>'):
            direction = 3
        elif(lst[row][col]=='^'):
            direction = 0
        elif(lst[row][col]=='v'):
            direction = 1

        elif(lst[row][col]=='_'):
            if(memory == 0):
                direction = 3
            else:
                direction = 2

        elif(lst[row][col] =='|'):
            if(memory == 0):
                direction = 1
            else:
                direction = 0

        elif(lst[row][col]=='?'):
            direction = 4 

        elif(lst[row][col] in ['0','1','2','3','4','5','6','7','8','9']):
            memory = int(lst[row][col])

        elif(lst[row][col]=='+'):
            memory+=1

            if(memory==16):
                memory = 0
        elif(lst[row][col]=='-'):
            memory-=1

            if(memory==-1):
                memory = 15

        
        if(direction == 0):
            n_row = row -1
            n_col = col

            if(n_row == -1):
                n_row = R - 1

            if((n_row,n_col,direction,memory) not in visited):
                visited[(n_row,n_col,direction,memory)]=1
                queue.append((n_row,n_col,direction,memory))

        elif(direction == 1):
            n_row = row + 1
            n_col = col

            if(n_row == R):
                n_row = 0

            if((n_row,n_col,direction,memory) not in visited):
                visited[(n_row,n_col,direction,memory)]=1
                queue.append((n_row,n_col,direction,memory))
        
        elif(direction == 2):
            n_row = row 
            n_col = col - 1

            if(n_col == -1):
                n_col = C - 1

            if((n_row,n_col,direction,memory) not in visited):
                visited[(n_row,n_col,direction,memory)]=1
                queue.append((n_row,n_col,direction,memory))

        elif(direction == 3):
            n_row = row 
            n_col = col + 1 
            if(n_col == C):
                n_col = 0   
            if((n_row,n_col,direction,memory) not in visited):
                visited[(n_row,n_col,direction,memory)]=1
                queue.append((n_row,n_col,direction,memory))

        else:

            for direc in range(4):

                if(direc==0):
                    n_row = row -1
                    n_col = col
        
                    if(n_row == -1):
                        n_row = R - 1

                elif(direc==1):
                    n_row = row + 1
                    n_col = col
        
                    if(n_row == R):
                        n_row = 0

                elif(direc == 2):
                    n_row = row 
                    n_col = col -1
        
                    if(n_col == -1):
                        n_col = C - 1
                else:
                    n_row = row
                    n_col = col + 1

                    if(n_col == C):
                        n_col = 0

                if((n_row,n_col,direction,memory) not in visited):
                    visited[(n_row,n_col,direc,memory)]=1
                    queue.append((n_row,n_col,direc,memory))


    return 'NO'
    
for test_case in range(1,T + 1):

    R, C = map(int,input().split())

    lst= [list(input()) for _ in range(R)]

    memory = 0
    
    #direction = 0  # 0, 1, 2 ,3, 4 direction이 4면 4방향 다 해보기

    visited = {}

    queue = deque()

    ans = bfs()

    

    print(f"#{test_case} {ans}")
    
    