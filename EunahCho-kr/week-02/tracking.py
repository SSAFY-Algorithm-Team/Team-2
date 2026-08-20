# swea 1953 탈주범 검거
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
# 소요 시간 : 4h/ 시도 : 6

from collections import deque


DIRECTIONS = {
    1: [(0, 1), (1, 0), (0, -1), (-1, 0)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(0, 1), (1, 0)],
    6: [(0, -1), (1, 0)],
    7: [(-1, 0), (0, -1)],
}


def solve(n, m, r, c, l, board):
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    que = deque([(r, c, 1)])
    while que:
        x, y, t = que.popleft()

        if t == l: 
            break

        pipe = board[x][y]
        # print("pipe", p)

        for dx, dy in DIRECTIONS[pipe]:
            nx, ny = x + dx, y + dy
            # print("탐색 시작 dx, dy : ", dx, dy)
            # print("nxny : ", nx, ny)

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] and not visited[nx][ny]:
                next_pipe = board[nx][ny]
                if next_pipe:
                    # print("nxny_after_1st_condi : ", nx, ny)
                    opp_dx, opp_dy = -dx , -dy
                    if (opp_dx, opp_dy) in DIRECTIONS[board[nx][ny]]: # 지금 진행 방향의 반대 방향을 새로운 파이프가 갖고 있다면
                    # print("nxny_after_2nd_condi : ", nx, ny)
                        visited[nx][ny] = True
                        que.append((nx, ny, t + 1))
                        # print(que)

    answer = sum([sum(visited[i]) for i in range(n)])
    return answer


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        n, m, r, c, l = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        answer = solve(n, m, r, c, l, board)
        print(f"#{test_case} {answer}")


if __name__ == "__main__":
    main()