#0은 통로 1은 벽 2는 출발 3은 도착


def find_start():

    for row in range(N):
        for col in range(N):
            if(lst[row][col]=='2'):
                return row,col

DIRECTION = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(row,col,cnt):

    visited[row][col]=True
    global ans
    for r , c in DIRECTION:

        n_row = row + r
        n_col = col + c

        if(0 <= n_row < N and 0 <= n_col < N):
            if(visited[n_row][n_col]):
                continue
            
            if(lst[n_row][n_col]=='3'):
                
                ans= min(ans,cnt)
                return 

            if(lst[n_row][n_col]=='1'):
                continue

            if(lst[n_row][n_col]=='0'):
                dfs(n_row,n_col,cnt+1)

        
T=int(input())

for test_case in range(1,T + 1):

    N = int(input())

    lst= [list(input()) for _ in range(N)]

    visited= [[False]*N for _ in range(N)]

    start_row, start_col = find_start()

    ans=10**9

    dfs(start_row,start_col,0)

    if(ans==10**9):
        ans=0

    print(f"#{test_case} {ans}")
        