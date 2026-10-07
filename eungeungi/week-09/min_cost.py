def find(N,arr):
    visited = [False] * N
    mini = float('inf')

    def dfs(i,cost):
        nonlocal mini
        if cost >= mini:
            return
        if i == N:
            mini = min(mini, cost)
            return

        for j in range(N):
            if visited[j]:
                continue

            visited[j] = True
            dfs(i+1,cost+arr[i][j])
            visited[j] = False
    dfs(0,0)
    return mini

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        row = list(map(int,input().split()))
        arr.append(row)
    ans = find(N,arr)
    print(f"#{tc} {ans}")