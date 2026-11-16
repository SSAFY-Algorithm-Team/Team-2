# SWEA 2817 부분수열의 합
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE&problemTitle=2817&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 50m / 2회

import sys


def dfs(idx, path):
    global cnt

    # print(path)

    if sum(path) == K:
        cnt += 1
        return

    if idx == N:
        return

    dfs(idx + 1, path + [nums[idx]])
    dfs(idx + 1, path)


sys.stdin = open ('2817_input.txt')
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    dfs(0, [])

    print(f"#{tc} {cnt}")


    