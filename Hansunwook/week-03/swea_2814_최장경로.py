T = int(input())
for test_case in range(1, T + 1):
    # 초기 접근
    # 지나간 정점을 세는 문제와 다름이 없다고 생각한다..
    # 그래서 점 하나씩 잡고 계속 깊이 들어가는 식으로..?
    # 일단 dfs로 구현
    # 안에서는 하나 잡고 그 다음 연결되면 계속 이어나가고 끝이면 전으로 돌아와서 다시 탐색하는 느낌으로?
    
    N, M = map(int, input().split())
    adj = [[False] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x][y] = True
        adj[y][x] = True

    visit = [False] * (N + 1)
    max_len = [0]

    def dfs(cur, length):
        if max_len[0] < length:
            # print("################그래프 하나 완료")
            # print("max값 업데이트")
            max_len[0] = length
        for nxt in range(1, N + 1):
            # print(i,"위치 잡고 시작중....")
            if not visit[nxt] and adj[cur][nxt]:
                visit[nxt] = True
                dfs(nxt, length + 1)
                visit[nxt] = False

    for start in range(1, N + 1):
        visit[start] = True
        dfs(start, 1)
        visit[start] = False

    print(f"#{test_case} {max_len[0]}")