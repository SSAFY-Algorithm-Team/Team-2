from collections import deque

DIRECTION = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

def bfs(row,col):

    num_room = 0 # 얘 이따가 리턴값임

    queue= deque()
    queue.append((row,col))
    visited[row][col] = True 

    while(queue):

        c_row, c_col = queue.popleft()

        for r , c in DIRECTION:

            n_row = c_row + r
            n_col = c_col + c

            if(0<=n_row<n and 0<=n_col<n and lst[n_row][n_col]==1):
                if(not visited[n_row][n_col]):
                    num_room += 1
                    visited[n_row][n_col] = True
                    queue.append((n_row,n_col))

    return num_room

n= int(input())

lst = [list(map(int,input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

n_houses = 0
lst_ans = []

for row in range(n):
    for col in range(n):

        if(lst[row][col]==1 and not visited[row][col]):
            n_houses += 1
            t=bfs(row,col)
            lst_ans.append(t)

lst_ans.sort()

print(n_houses)

for k in lst_ans:
    print(k+1)


        
