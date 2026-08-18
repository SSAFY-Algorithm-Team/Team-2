# programmers 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 소요시간 : 1h 10m / 시도 : 3

from collections import deque
DIRECIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    que = deque([(0, 0, 1)]) # 시작 지점 (0, 0) / 지나온 칸 개수 1
    visited = [[0] * m for _ in range(n)]
    min_dist = float('inf')

    while que:
        x, y, d = que.popleft()
        # print(x, y, d)
        if x == n - 1 and y == m - 1:
            min_dist = min(min_dist, d)

        for dx, dy in DIRECIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                que.append((nx, ny, d + 1))
                visited[nx][ny] = 1


    if min_dist == float('inf'):
        return -1
    else:
        return min_dist


# print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))