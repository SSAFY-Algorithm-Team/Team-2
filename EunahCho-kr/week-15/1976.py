# BOJ 1976 여행 가자
# https://acmicpc.net/problem/

"""
유니온파인드로 길 연결
-> 연결됐는지 아닌지 확인
"""


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


def check():
    for i in range(M - 1):
        now = itinery[i]
        nxt = itinery[i + 1]
        if find(now) != find(nxt):
            return 'NO'
    return 'YES'


N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
itinery = list(map(int, input().split()))

parent = [i for i in range(N + 1)]

for x in range(N):
    for y in range(x + 1, N):
        if arr[x][y]:
            union(x + 1, y + 1)

ans = check()
print(ans)
