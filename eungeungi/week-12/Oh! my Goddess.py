from collections import deque
def demon(N,M,arr,start,dem):
    queue = deque()
    queue.append((start[0],start[1],0))

    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True

    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    # 악마의 손아귀
    def trans(arr):

        for _ in range(len(dem)):
            x,y = dem.popleft()            
            for dx, dy in dir:
                nx, ny = x+dx, y+dy

                if 0<= nx < N and 0<= ny < M:
                    if arr[nx][ny] == '.':
                        arr[nx][ny] = '*'
                        dem.append((nx,ny))

    # 수연이 첫 위치도 .으로 바꾸기
    arr[start[0]][start[1]] = '.'
    while queue:
        trans(arr)
        for _ in range(len(queue)):
            x,y,cnt = queue.popleft()

            if arr[x][y] == '*':
                continue
        
            for dx, dy in dir:
                nx, ny = x+dx, y+dy
                if 0<= nx< N and 0<= ny < M:
                    if arr[nx][ny] =='D':
                        return cnt + 1
                
                    if arr[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx,ny,cnt+1))
    return 'GAME OVER'


T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = []
    dem = deque()
    for i in range(N):
        row = list(input())
        for j in range(M):
            if row[j] == 'S':
                start = (i,j)
            elif row[j] =='*':
                dem.append((i,j))
        arr.append(row)
    ans = demon(N,M,arr,start,dem)
    print(f"#{tc} {ans}")