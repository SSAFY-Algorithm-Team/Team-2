# SWEA 1861 정사각형 방
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc
# 어쨌든 한 길로만 갈 수 있으므로 dfs 탐색이 나을 수도 있다는 아이디어 ==> ㅋㅋ 실패

import sys

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def solve(n, rooms):
    max_cnt = 0

    visited = [[1] * n for _ in range(n)]

    def dfs(depth, r, c):
        nonlocal max_cnt

        if visited[r][c] != 1:
            cnt = depth + visited[r][c]
            max_cnt = max(cnt, max_cnt)
            return

        if depth == n ** 2:
            return

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                visited[nr][nc] = visited[r][c] + 1
                dfs(depth + 1, nr, nc)

    dfs(0, 0, 0)

    print(visited)

    max_dist = max(row for row in visited)
    best_start = n ** 2
    for x in range(n):
        for y in range(n):
            if visited[x][y] == max_dist:
                best = rooms[x][y]
                best_start = min(best_start, best)

    return best_start, max_cnt


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