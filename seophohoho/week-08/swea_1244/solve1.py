import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    ns, cnt = input().split()
    cnt = int(cnt)
    n = len(ns)

    states = {ns}
    for _ in range(cnt):
        nxt = set()
        for s in states:
            arr = list(s)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    arr[i], arr[j] = arr[j], arr[i]
                    nxt.add("".join(arr))
                    arr[i], arr[j] = arr[j], arr[i]
        states = nxt

    print(f"#{tc} {max(states)}")
