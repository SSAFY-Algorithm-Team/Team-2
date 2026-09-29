# 7465. 창용마을 무리 개수 (D4)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU&
# 소요시간 50m / 시도 3

import sys


def make_set(n):
    return list(range(n + 1))


def find_set(x, parent):
    # print(x)
    if x == parent[x]:
        return x
    
    parent[x] = find_set(parent[x], parent)
    return parent[x]


def union_set(x, y, parent):
    rx = find_set(x, parent)
    ry = find_set(y, parent)

    if rx != ry:
        parent[ry] = rx


def main():
    sys.stdin = open('7456_input.txt')
    t = int(input())
    for tc in range(1, t + 1):
        n, m = map(int, input().split())
        parent = make_set(n)
        for _ in range(m):
            x, y = map(int, input().split())
            union_set(x, y, parent)

        for x in range(1, n + 1): # 마지막으로 한 번 더 find set 해야 평탄화 완료됨
            find_set(x, parent)

        # print(parent)
        
        ans = len(set(parent)) - 1
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    main()