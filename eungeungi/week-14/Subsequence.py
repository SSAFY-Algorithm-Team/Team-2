def find(N,arr):
    visited = [False] * N
    maxi = 0
    def dfs(idx, prob):
        nonlocal maxi
        if idx ==N:
            maxi = max(maxi, prob)
            return
        if prob <= maxi:
            return
        for j in range(N):
            if not visited[j]:
                visited[j] = True

                dfs(idx+1, prob* arr[idx][j]/100)
                visited[j] = False
    dfs(0,100)

    return maxi


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        row = list(map(int,input().split()))
        arr.append(row)
    
    ans = find(N,arr)
    print(f"#{tc} {ans:.6f}")