import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    ns, cnt = input().split()
    cnt = int(cnt)
    n = len(ns)

    states = {ns}
    for _ in range(cnt):
        next_haha = set()
        for s in states:
            arr = list(s)
            for i in range(n):
                for j in range(n):
                    arr[i], arr[j] = arr[j], arr[i]
                    next_haha.add("".join(arr))
                    arr[i], arr[j] = arr[j], arr[i]
        states = next_haha

    print(f"#{tc} {max(states)}")
