import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    daily, monthly, quarterly, yearly = map(int, input().split())
    days = list(map(int, input().split()))

    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = dp[i - 1] + days[i - 1] * daily
        dp[i] = min(dp[i], dp[i - 1] + monthly)
        dp[i] = min(dp[i], dp[max(0, i - 3)] + quarterly)

    answer = min(dp[12], yearly)
    print(f"#{tc} {answer}")
