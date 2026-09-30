import sys
sys.stdin = open("input.txt", "r")


def dfs(arr, depth):
    global answer
    key = ("".join(arr), depth)
    if key in visited:
        return
    visited.add(key)

    if depth == cnt:
        answer = max(answer, int(key[0]))
        return

    for i in range(n - 1):
        for j in range(i + 1, n):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(arr, depth + 1)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for tc in range(1, T + 1):
    ns, cnt = input().split()
    cnt = int(cnt)
    n = len(ns)

    visited = set()
    answer = 0
    dfs(list(ns), 0)

    print(f"#{tc} {answer}")
