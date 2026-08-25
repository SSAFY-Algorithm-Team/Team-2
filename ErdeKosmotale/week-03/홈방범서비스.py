
#풀이시간 1시간 30분 

# K의 범위설정으로 인해 많이 헤매었음.

########################################

#2K**2 -2K +1

#저 영역은 BFS로 계산 가능

#운영비용은 K값에 의해 먼저 결정

#손해를 안보면서 가장 많은 집에 서비스를 제공할수 있는 영역 찾기

#출력값은 제공받는 집 수

#보안회사 이익 = [서비스를 통해 얻는 이익]- 운영 비용(K)

from collections import deque

def bfs(lst,row,col,m,k,visited):

    n=len(lst)

    queue=deque()
    queue.append((row,col,1))
    visited[row][col]=True

    direction=[[-1,0],[1,0],[0,-1],[0,1]] #상 하 좌 우

    sum_profit=0 if lst[row][col]==0 else m
    n_visit=0 if lst[row][col]==0 else 1

    while(queue):

        c_row,c_col,c_k=queue.popleft()
        if(c_k==k):continue

        for r,c in direction:

            n_row=c_row+r
            n_col=c_col+c
            
            if(n_row<0 or n_row>=n or n_col<0 or n_col >=n):
                continue

            if(lst[n_row][n_col]==1 and visited[n_row][n_col]==False):
                sum_profit+=(m)
                n_visit+=1

            if(visited[n_row][n_col]==False):
                visited[n_row][n_col]=True
                queue.append((n_row,n_col,c_k+1))

    return (n_visit, (sum_profit-k**2 -(k-1)*(k-1)))


T = int(input())

for test_case in range(1, T + 1):

    n, m = map(int,input().split()) # 도시영역 크기, 집마다 지불 돈

    lst=[list(map(int,input().split())) for _ in range(n)]

    ans_visit=0
    ans=0

    

    for t in range(1,n+2):
        for row in range(n):
            for col in range(n):

                visited=[[False]*n for _ in range(n)]
                n_visit_inter, ans_inter=bfs(lst,row,col,m,t,visited)

                if(ans_inter<0):
                    continue

                ans_visit=max(ans_visit,n_visit_inter)
                    

    print(f"#{test_case} {ans_visit}")

