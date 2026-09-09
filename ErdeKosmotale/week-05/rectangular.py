
from collections import deque

def bfs(row,col):

    global ans
    global ans_room_number

    visited=[[0]*n for _ in range(n)]

    queue=deque()
    queue.append((row,col))

    visited[row][col]=True
    now_room_number=lst[row][col]

    ans_inter=1

    direction=[(-1,0),(1,0),(0,-1),(0,1)]


    while(queue):

        c_row, c_col= queue.popleft()

        for r,c in direction:
            n_row=c_row+r
            n_col=c_col+c

            if(0<=n_row<n and 0<=n_col<n and visited[n_row][n_col]==False):
                if(lst[n_row][n_col]-lst[c_row][c_col]==1):            
                    ans_inter += 1
                    queue.append((n_row,n_col))
                    visited[n_row][n_col]=True

    if((ans_inter) == (ans)):
        ans_room_number=min(ans_room_number,now_room_number)

    elif(ans_inter>ans):
        ans=ans_inter
        ans_room_number=now_room_number
            

    return


    
        
T=int(input())

for test_case in range(1,T+1):

    n=int(input())

    lst=[list(map(int,input().split())) for _ in range(n)]
    
    ans=1

    ans_room_number=-1


    for row in range(n):
        for col in range(n):
            bfs(row,col)

    print(f"#{test_case} {ans_room_number} {ans}")

    