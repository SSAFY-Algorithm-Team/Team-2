
from collections import deque



# 한번 꺾으면 그거는 또 못쓰게 해야겠네요
# 들렀던 곳 디저트 번호도 추적해야 할듯

# 사용한 direction 번호, 들렀던 곳 디저트 번호 추적하는 리스트 사용 현재가는 방향도 있어야 함

def bfs(row,col):

    direction=[(-1,-1),(-1,1), (1,-1), (1, 1)]  #좌상,우상,좌하,우하
    #now_direction도 0, 1, 2, 3으로 사용합니다.
    
    queue=deque()
    queue.append((row,col,0,-1,direction_use,desert_check)) #row,col, 현재 점수, 이전 이동방향, 사용한 direction lst, 먹은 디저트 lst 

    while(queue):

        c_row, c_col, score, now_direction, c_direction_use, c_desert_check= queue.popleft()

        for idx,r,c in enumerate(direction):

            n_row=c_row+r
            n_col=c_col+c

            if(idx!=now_direction and idx in c_direction_use):  
                continue

            if()

            if(n_row<0 or n_row>=n or n_col <0 or n_col>=n):
                continue

            if(lst[n_row][n_col] in c_desert_check):
                continue


            
    
T=int(input())

for test_case in range(1,T+1):

    direction_use= [] #사용한 direction 추적
    desert_check = [] #들렀던 디저트 목록들 추적

    n=int(input())

    lst=[list(map(int,input().split())) for _ in range(n)]
    

    


    