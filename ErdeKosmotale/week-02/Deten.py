#1 상하좌우  #3좌우   #5 하 우 #7 상 좌
#2 상하     #4 상우  #6 하 좌



from collections import deque

def bfs(lst,visited,h_row,h_col,L):
    direction=[(),((-1,0),(1,0),(0,-1),(0,1)),
           ((-1,0),(1,0)),
           ((0,-1),(0,1)),
           ((-1,0),(0,1)),
           ((1,0),(0,1)),
           ((1,0),(0,-1)),
           ((-1,0),(0,-1))
           ]
    queue=deque()
    queue.append((h_row,h_col,1))

    while(queue):

        row,col,L_inter=queue.popleft()

        if(L_inter==L):
            continue

        type_hose=lst[row][col]

        if(type_hose==0):
            continue

        for r,c in direction[type_hose]:
            n_row=row+r
            n_col=col+c

            if(n_row>=0 and n_row<len(lst) and n_col>=0 and n_col<len(lst[0])):
                if(visited[n_row][n_col]==0):
                    visited[n_row][n_col]=1
                    queue.append((n_row,n_col,L_inter+1))

    return 

T = int(input())

for test_case in range(1, T + 1):
    
    n,m,h_row,h_col,L=map(int,input().split())

    lst=[list(map(int,input().split())) for _ in range(n)]

    visited=[[0]*m for _ in range(n)]

    bfs(lst,visited,h_row,h_col,L)

    ans=0

    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if(visited[i][j]==1):
                ans+=1

    print(f"#{test_case} {ans}")
            
