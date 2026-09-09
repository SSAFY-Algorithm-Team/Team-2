def find(N,arr):
    pos = [None] * (N*N +1)
    for i in range(N):
        for j in range(N):
            pos[arr[i][j]] = (i,j)

    start = 1
    maxi = 1

    cur_start = 1
    cur_len = 1

    for num in range(1,N*N):
        x1, y1 = pos[num]
        x2, y2 = pos[num+1]

        if abs(x1-x2) + abs(y1-y2) == 1:
            cur_len +=1

        else:
            if cur_len > maxi:
                maxi = cur_len
                start = cur_start

            elif cur_len == maxi:
                start = min(start, cur_start)

            cur_start = num + 1
            cur_len = 1

    if cur_len >maxi:
        maxi = cur_len
        start = cur_start

    elif cur_len == maxi:
        start = min(start, cur_start)

    return start, maxi
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr =[]
    for _ in range(N):
        row = list(map(int,input().split()))
        arr.append(row)
    start, maxi = find(N,arr)
    print(f"#{tc} {start} {maxi}")





def find(N,arr):
    dir = [(-1,0),(0,1),(1,0),(0,-1)]

    def dfs(i,j):
        res = 1
        cur = arr[i][j]

        for x,y in dir:
            nx = i+x
            ny = j+y

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == cur + 1:
                    res = 1 + dfs(nx,ny)

        return res

    maxi = 1
    start = arr[0][0]

    for i in range(N):
        for j in range(N):
            length = dfs(i,j)

            if length > maxi:
                maxi = length
                start = arr[i][j]

            elif length == maxi:
                if arr[i][j] < start:
                    start = arr[i][j]

    return start, maxi


T = int(input())

for tc in range(1,T+1):
    N = int(input())

    arr = []

    for _ in range(N):
        row = list(map(int,input().split()))
        arr.append(row)

    start, maxi = find(N,arr)

    print(f"#{tc} {start} {maxi}")
