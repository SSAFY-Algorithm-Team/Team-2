# 4014. [모의 SW 역량테스트] 활주로 건설
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH&categoryId=AWIeW7FakkUDFAVH&categoryType=CODE&problemTitle=4014&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 936~

import sys
sys.stdin = open('4014_input.txt', 'r')


def check(row, n, x):
    idx = 1
    seq = 1

    while idx < n:
        diff = row[idx] - row[idx - 1]
        if diff == 0:
            seq += 1
        elif diff == 1:
            if seq < x:
                # print(seq, "up failed")
                return False
            seq = 1
        elif diff == -1:
            if idx + x - 1 > n - 1:
                # print(idx+x, "down, oor")
                return False
            for _ in range(x - 1):
                idx += 1
                diff_tmp = row[idx] - row[idx - 1]
                if diff_tmp:
                    # print("down, height diff")
                    return False
            seq = 0
        else:
            # print(row[idx], row[idx -1], "diff more than 2")
            return False
        idx += 1

    return True

        
def solve(board, n, x):
    ans = 0
    # 가로
    for row in board:
        # print("가로", row)
        if check(row, n, x):
            # print("pass")
            ans += 1

    # 세로
    for col in zip(*board):
        # print("세로", col)
        if check(col, n, x):
            # print("pass")
            ans += 1

    return ans


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = solve(board, N, X)
    print(f"#{tc} {ans}")