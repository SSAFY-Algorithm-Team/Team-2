
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    answer = float('inf')

    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, total_cost):
        global answer

        # 가지치기: 이미 최소 비용 이상이라면 중단
        if total_cost >= answer:
            return

        # 목적지 도착
        if x == N - 1 and y == N - 1:
            answer = min(answer, total_cost)
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 지도 범위를 벗어난 경우
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            # 현재 경로에서 이미 방문한 경우
            if visited[nx][ny]:
                continue

            # 이동 비용 계산 
            height_diff = heights[nx][ny] - heights[x][y]
            move_cost = 1 + max(0, height_diff)

            visited[nx][ny] = True

            dfs(nx, ny, total_cost + move_cost)

            # 백트래킹: 방문 상태 복구
            visited[nx][ny] = False

    visited[0][0] = True
    dfs(0, 0, 0)

    print(f"#{tc} {answer}")
