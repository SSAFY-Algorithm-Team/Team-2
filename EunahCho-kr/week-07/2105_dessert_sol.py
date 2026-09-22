# 2105 SWEA [모의 SW 역량테스트] 디저트 카페
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# 소요시간 1h / 시도 1


import sys


def check(r, c, n1, n2, board):
    desserts = set()
    n = len(board)
    dir = [(1, 1)] * n1 + [(1, -1)] * n2 + [(-1, -1)] * n1 + [(-1, 1)] * n2
    # print(dir)

    for dr, dc in dir:

        # print(r, c)
        
        if r > n - 1 or r < 0  or c > n - 1 or c < 0:
            # print("out")
            return False

        if board[r][c] in desserts:
            # print("duplicated")
            return False
        
        desserts.add(board[r][c])

        r += dr
        c += dc

    return True


def solve(n, board):

    path_n = 2 * (n - 1)
    while path_n >= 4:
        # print(path_n)
        # 현재 대각선 길이에서 모든 시작점 기준 탐색
        # 시작점 -> 2중 for문 탐색

        for r in range(n):
            for c in range(n):
                n1 = path_n // 2 - 1 # 양의 방향 대각선 길이
                n2 = 1 # 음의 방향 대각선 길이
                # 모양변형
                while n1 >= 1 and n2 < path_n // 2: # 여기 조건 다시 손보기
                    if check(r, c, n1, n2, board):
                        return 2 * (n1 + n2)
                    # print(n1, n2)
                    n1 -= 1
                    n2 += 1

        # 안되면 크기 줄임
        path_n -= 2

    return -1



def main():
    sys.stdin = open('2105_input.txt', 'r')
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        ans = solve(n, board)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    main()