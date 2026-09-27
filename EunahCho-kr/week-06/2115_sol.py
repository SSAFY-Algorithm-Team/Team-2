# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZ9kDS86wCTHBITH&contestProbId=AV5V4A46AdIDFAWu&probBoxId=AZ9kECgawDHHBITH&type=PROBLEM&problemBoxTitle=DFS&problemBoxCnt=6

import sys
from itertools import combinations


def solve(n, m, c, honeys):
    visited = [[False] * n for _ in range(n)]  # 시작점 기준만 처리 (다음에 가는 곳에서 겹칠 수 있으므로)
    segments = []  # [(x, y, 현재 사이클 대이익), ...] 으로 저장

    def dfs(x, y):  # (x, y)가 시작점
        nonlocal c
        # print(x, y)

        if y + m > n or x >= n:  # 끝에 도달
            return

        if not visited[x][y]:
            arr = honeys[x][y: y + m]

            # 시작점만 방문 처리
            visited[x][y] = True

            curr_max_profit = 0
            for k in range(1, m + 1):  # 크기가 1, 2, 3, ..., m 일 때 조합을 다 살펴봐야함
                for comb in combinations(arr, k):
                    square = 0
                    if sum(comb) <= c:
                        for com in comb:
                            square += com * com
                        curr_max_profit = max(square, curr_max_profit)

            segments.append((x, y, curr_max_profit))

        dfs(x, y + 1)
        dfs(x + 1, y)

    dfs(0, 0)

    ans = 0
    p_n = len(segments)
    for i in range(p_n):
        x1, y1, p1 = segments[i]
        for j in range(i + 1, p_n):
            x2, y2, p2 = segments[j]

            if x1 == x2:  # 같은 행에서 y 값들이 겹치면 안됨 -> 넘어감
                if not (y1 + m <= y2 or y2 + m <= y1):
                    continue

            ans = max(ans, p1 + p2)

    return ans


def main():
    sys.stdin = open('input.txt', 'r')
    T = int(input())
    for tc in range(1, T + 1):
        N, M, C = map(int, input().split())
        honeys = [list(map(int, input().split())) for _ in range(N)]
        ans = solve(N, M, C, honeys)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    main()
