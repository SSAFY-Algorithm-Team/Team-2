from collections import deque

def bfs(lst):
    
    n=len(lst)
    m=len(lst[0])
    
    direction=((-1,0),(1,0),(0,-1),(0,1))
    
    queue=deque()
    queue.append((0,0,1))

    visited=[[0]*m for _ in range(n)]
        
    while(queue):
        
        row,col,d=queue.popleft()
        
        for _,R in enumerate(direction):
            
            r=R[0]
            c=R[1]
            
            n_row=row+r
            n_col=col+c
            if(n_row==n-1 and n_col==m-1):
                return d+1
            
            if(n_row>=0 and n_row<n and n_col>=0 and n_col<m):
                if(lst[n_row][n_col]>1 and visited[n_row][n_col]==0):
                    if(d+1<lst[n_row][n_col]): #여기 등호를 포함하는지가 굉장히 주요했습니다.
                        lst[n_row][n_col]=d+1
                        queue.append((n_row,n_col,d+1))
    
                
                elif(lst[n_row][n_col]==1 and visited[n_row][n_col]==0):
                        lst[n_row][n_col]=d+1
                        queue.append((n_row,n_col,d+1))
                        visited[n_row][n_col]=1
                else:continue
                print(d+1,n_row,n_col)
    return -1
    
def solution(maps):
    answer = bfs(maps)
    
    return answer
