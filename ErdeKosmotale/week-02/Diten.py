#1 상하좌우  #3 좌우  #5 하 우 #7 상 좌
#2 상하     #4 상우  #6 하 좌


#탈주범 검거, swea D4
#소요시간: 1시간 20분 
#전체 50개에서 49개만 맞는 경우가 지속되고 있는데.. 원인을 못찾고 있음.

from collections import deque

def bfs(lst,visited,h_row,h_col,L):
    direction=[
           ((-1,0),(1,0),(0,-1),(0,1)),
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

        type_hose=lst[row][col]-1

        if(type_hose==-1):
            continue

        for r,c in direction[type_hose]:
            n_row=row+r
            n_col=col+c

            if(n_row>=0 and n_row<len(lst) and n_col>=0 and n_col<len(lst[0])):

                if(r==-1 and c==0):
                    if(lst[n_row][n_col] in (3,4,7)):
                        continue

                elif(r==1 and c==0):
                    if(lst[n_row][n_col] in (3,5,6)):
                        continue

                elif(r==0 and c==-1):
                    if(lst[n_row][n_col] in (2,6,7)):
                        continue

                elif(r==0 and c==1):
                    if(lst[n_row][n_col] in (2,4,5)):
                        continue
                    
                if(lst[n_row][n_col]==0 or visited[n_row][n_col]==1):

                    continue
                
                visited[n_row][n_col]=1
                queue.append((n_row,n_col,L_inter+1))
    
    return

T = int(input())

for test_case in range(1, T + 1):
    
    n,m,h_row,h_col,L=map(int,input().split())

    lst=[list(map(int,input().split())) for _ in range(n)]

    visited=[[0]*m for _ in range(n)]

    k=bfs(lst,visited,h_row,h_col,L)

    ans=0

    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if(visited[i][j]==1):
                ans+=1

    if(L==1):
        ans=1

    print(f"#{test_case} {ans}")
            
