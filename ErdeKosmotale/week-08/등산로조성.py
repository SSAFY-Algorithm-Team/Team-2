# 등산로는 가장 높은 봉우리에서 시작
# 높 -> 낮 가로 또는 세로 방향 연결 되어야 함
# 대각선 안됨.
# K만큼 깎는 공사 가능
# bfs로 가장 깊게 갈 수 있는 경우 탐색 함수



# 전 이걸 문제 오류라고 생각합니다. 정말정말 !


from collections import deque

DIRECTION = [(-1,0),(1,0), (0,-1), (0,1)] # 상 하 좌 우

def bfs(lst_t, row, col):

    lst = [row[:] for row in lst_t]

    max_depth = -30
    queue = deque()
    queue.append((row,col,0))
    
    while(queue):

        c_row, c_col, depth_now = queue.popleft()

        max_depth = max(max_depth,depth_now)

        for r, c in DIRECTION:

            n_row = c_row + r
            n_col = c_col + c

            if(0 <= n_row < N and 0 <= n_col < N):
                if(lst[n_row][n_col] < lst[c_row][c_col]):
                    queue.append((n_row,n_col,depth_now+1))
                    

    return max_depth

def find_max_grid(lst):

    max_value = 0

    max_grids=[]

    for r in range(N):
        for c in range(N):
            max_value = max(max_value,lst[r][c])

    for r in range(N):
        for c in range(N):
            if(lst[r][c]==max_value):
                max_grids.append((r,c))

    return max_grids

T = int(input())

for test_case in range(1,T+1):

    ans = 0

    N, K = map(int,input().split())

    lst = [list(map(int,input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            max_grid = find_max_grid(lst)
            for i in range(0,K+1):
                lst[r][c]-=i
                
                for row,col in max_grid:
                    ans=max(ans,bfs(lst,row,col))

                lst[r][c]+=i

    if(ans==0):
        print(f"#{test_case} {ans}")

    else:
        print(f"#{test_case} {ans+1}")
