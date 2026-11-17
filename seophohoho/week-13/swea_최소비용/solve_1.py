import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        cost, r, c = heapq.heappop(pq)
        if cost > dist[r][c]:
            continue
        if r == N - 1 and c == N - 1:
            break
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                nxt = cost + 1 + max(0, grid[nr][nc] - grid[r][c])
                if nxt < dist[nr][nc]:
                    dist[nr][nc] = nxt
                    heapq.heappush(pq, (nxt, nr, nc))

    answer = dist[N - 1][N - 1]
    print(f"#{tc} {answer}")
