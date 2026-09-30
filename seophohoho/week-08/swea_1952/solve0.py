import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    daily, monthly, quarterly, yearly = map(int, input().split())
    days = list(map(int, input().split()))

    total = sum(min(d * daily, monthly) for d in days)
    answer = min(total, yearly)

    print(f"#{tc} {answer}")
