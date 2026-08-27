def leng(g):
    n = len(g)
    visited = [False] * n
    maxi = 0
    def dfs(cur,cnt):
        nonlocal maxi

        visited[cur] = True
        maxi = max(maxi,cnt)

        for nxt in g[cur]:
            if not visited:
                dfs(nxt,cnt+1)
        visited[cur] = False

    for start in range(1,n):
        dfs(start,1)

    return maxi 
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    g = [set() for _ in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        g[a].add(b)
        g[b].add(a)
    ans = leng(g)
    print(f"#{tc} {ans}")