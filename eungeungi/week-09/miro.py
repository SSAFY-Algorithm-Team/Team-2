from collections import deque
def bfs(N,arr,queue):
    visited = [[False]*N for _ in range(N)]
    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    
    nx, ny,_  = queue[0]
    visited[nx][ny] = True

    while queue:
        nx, ny, d = queue.popleft()
        for x,y in dir:
            dx, dy = nx + x, ny + y

            if 0 <= dx < N and 0 <= dy <N:
                if arr[dx][dy] ==0 and not visited[dx][dy]:
                    visited[dx][dy] = True
                    queue.append((dx,dy,d+1))
                    
                if arr[dx][dy] == 3:
                    return d
    return 0
    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    queue = deque()
    for i in range(N):
        row = list(map(int,input().strip()))
        arr.append(row)
        for j in range(len(row)):
            if row[j] == 2:
                queue.append((i,j,0))
    ans = bfs(N,arr,queue)
    print(f"#{tc} {ans}")