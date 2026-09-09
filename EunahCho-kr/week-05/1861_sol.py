# SWEA 1861 정사각형 방
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc
# 소요시간 : 2h / 시도횟수 : 2
# 아 시간초과............................
# dfs 다시 해보기

import sys
from collections import deque


DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(rooms, start, n, visited):

    if visited[start[0]][start[1]]:
        return
    else:
        visited[start[0]][start[1]] = 1

    queue = deque([start]) # r, c

    while queue:
        # print(queue)
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < n:
                if rooms[nr][nc] - rooms[r][c] == 1:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    # return visited[r][c]

# print(bfs([[1, 2], [3, 4]], (0, 1), 2))


def solve(n, rooms):
    max_cnt = 0
    visited = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            bfs(rooms, (r, c), n, visited)

    for row in visited:
        print(row)
    print()
    for row in rooms:
        print(row)

    best_start = n ** 2
    max_cnt = 0
    for r in range(n):
        for c in range(n):
            max_cnt = max(max_cnt, visited[r][c])
            if visited[r][c] == 1:
                best_start = min(best_start, rooms[r][c])
    

            # if not cnt:
            #     cnt = 

            # if cnt > max_cnt:
            #     max_cnt = cnt
            #     best_start = rooms[r][c]
            # elif max_cnt == cnt:
            #     if best_start > rooms[r][c]:
            #         best_start = rooms[r][c]

    return best_start, max_cnt

# print(solve(2, [[1, 2], [3, 4]]))


def main():
    sys.stdin = open('1861_input.txt', 'r')
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        rooms = [list(map(int, input().split())) for _ in range(n)]
        ans = solve(n, rooms)
        print(f"#{tc} {ans[0]} {ans[1]}")


if __name__ == "__main__":
    main()

# ====================

""" bfs => 안됐음 (시간초과 + 몇 테케 틀림)
from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(rooms, start, n):
    queue = deque([(start[0], start[1], 1)]) # r, c, passed_rooms_cnt
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        # print(queue)
        r, c, cnt = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if rooms[nr][nc] - rooms[r][c] == 1:
                    queue.append((nr, nc, cnt + 1))

    return cnt

# print(bfs([[1, 2], [3, 4]], (0, 1), 2))
    

def solve(n, rooms):
    max_cnt = 0
    for r in range(n):
        for c in range(n):
            cnt = bfs(rooms, (r, c), n)

            if cnt > max_cnt:
                max_cnt = cnt
                best_start = rooms[r][c]

            elif max_cnt == cnt:
                if best_start > rooms[r][c]:
                    best_start = rooms[r][c]

    return best_start, max_cnt

# print(solve(2, [[1, 2], [3, 4]]))


def main():
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        rooms = [list(map(int, input().split())) for _ in range(n)]
        ans = solve(n, rooms)
        print(f"#{tc} {ans[0]} {ans[1]}")


if __name__ == "__main__":
    main()
"""
# ===============

""" 메모이제이션 시도 -> 테케 틀림..
from collections import deque


DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(rooms, start, n, visited):
    queue = deque([start]) # r, c

    if visited[start[0]][start[1]]:
        return
    else:
        visited[start[0]][start[1]] = 1

    while queue:
        # print(queue)
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if rooms[nr][nc] - rooms[r][c] == 1:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    return visited[r][c]

# print(bfs([[1, 2], [3, 4]], (0, 1), 2))


def solve(n, rooms):
    max_cnt = 0
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            cnt = bfs(rooms, (r, c), n, visited)
            if cnt:
                if cnt > max_cnt:
                    max_cnt = cnt
                    best_start = rooms[r][c]

                elif max_cnt == cnt:
                    if best_start > rooms[r][c]:
                        best_start = rooms[r][c]

    return best_start, max_cnt

# print(solve(2, [[1, 2], [3, 4]]))


def main():
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        rooms = [list(map(int, input().split())) for _ in range(n)]
        ans = solve(n, rooms)
        print(f"#{tc} {ans[0]} {ans[1]}")


if __name__ == "__main__":
    main()
    
"""