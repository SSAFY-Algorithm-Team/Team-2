# BOJ 2667 단지번호 붙이기
# https://acmicpc.net/problem/2667
# 30분 / 1회


"""
이중 for문으로 돌며 1 발견하면 bfs -> 간 곳은 visited 처리
bfs 끝나면 list에 지나온 넓이 저장
"""

from collections import deque


DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == '1' and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1

    return cnt


N = int(input())
board = [input() for _ in range(N)]
# print(board)
visited = [[False] * N for _ in range(N)]
result = []

for r in range(N):
    for c in range(N):
        if board[r][c] == '1' and not visited[r][c]:
            result.append(bfs((r, c)))

result.sort()

print(len(result))
for res in result:
    print(res)
