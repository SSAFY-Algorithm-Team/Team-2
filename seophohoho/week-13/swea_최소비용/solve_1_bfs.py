
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]

    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0

    queue = deque([(0, 0)])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            height_diff = heights[nx][ny] - heights[x][y]
            move_cost = 1 + max(0, height_diff)

            new_cost = dist[x][y] + move_cost

            # 더 적은 비용으로 도달할 수 있다면 갱신
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                queue.append((nx, ny))

    print(f"#{tc} {dist[N-1][N-1]}")
