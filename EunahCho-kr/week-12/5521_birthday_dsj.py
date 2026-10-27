# 5521. 상원이의 생일파티
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWO3kT6F2oDFAV4&categoryId=AWWO3kT6F2oDFAV4&categoryType=CODE&problemTitle=5521&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 서로소 집합 써보기


import sys


sys.stdin = open('5521_input.txt')


def make_set(n):
    return list(range(n + 1))


def find_set(x):
    if x == tree[x]:
        return x
    else:
        return find_set(tree[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_y != root_x:
        tree[root_y] = root_x


T = int(input())
for tc in range(1, T + 1):  
    N, M = map(int, input().split())
    pairs = [list(map(int, input().split())) for _ in range(M)]
    pairs.sort()
    # print(pairs)

    tree = make_set(N)

    tmp = set()
    for pair in pairs:
        if pair[0] == 1:
            tmp.add(pair[1])
            union(pair[0], pair[1])
        elif pair[0] in tmp:
            union(pair[0], pair[1])
        elif pair[1] in tmp: # [2, 3]인 pair에서 3이 상원이의 친구인 경우도 고려
            union(pair[1], pair[0])
        else:
            continue

    # print(tree)
    cnt = 0
    for t in tree:
        if t == 1:
            cnt += 1

    print(f"#{tc} {cnt - 1}")

