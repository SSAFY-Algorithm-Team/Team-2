import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    ns, cnt = map(int, input().split())
    digits = [int(d) for d in str(ns)]

    digits.sort(reverse=True)

    answer = int("".join(map(str, digits)))

    print(f"#{tc} {answer}")