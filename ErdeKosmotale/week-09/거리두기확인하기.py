# 대기실은 5개
# P 사람 , 0 빈테이블, X 파티션
# 현재 좌표가 'P'면 맨헤튼거리가 2인 지점은 다 봐야함

from collections import deque

DIRECTION = [(-1,0), (1,0), (0,-1), (0,1)] # 상 하 좌 우

def bfs(lst,row,col):
    
    queue = deque()
    visited= [[False]*5 for _ in range(5)]
    visited[row][col]= True
    
    queue.append((row,col,0))
    
    while(queue):
        
        c_row , c_col , d = queue.popleft()
        
        if(d>=2):
            continue
        
        for r , c in DIRECTION:
            
            n_row = c_row + r
            n_col = c_col + c
            
            
            if(0<=n_row<5 and 0<=n_col<5):
                
                if(not visited[n_row][n_col] and lst[n_row][n_col]=='P'):
                    
                    return 0
                
                if(lst[n_row][n_col]=='O'):
                    
                    if(not visited[n_row][n_col]):    
                        visited[n_row][n_col]=True
                        queue.append((n_row,n_col,d+1))
                        
    return 1
        
def solution(places):
    
    answer = [1]*len(places)
    
    for i in range(len(places)):
        
        place = places[i]
        
        flag=True
        for row in range(5):
            
            if(flag==False):
                break
            for col in range(5):
                if(flag==False):
                    break
                    
                if(place[row][col]=='P'):
                    flag = bfs(place,row,col)
                    
            if(flag==False):
                answer[i] = 0
                
                
    return answer