def solution(n):
    MOD = 1_000_000_007

    if n == 1:
        return 1
    if n == 2:
        return 2

    a = 1  # dp[1]
    b = 2  # dp[2]

    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD

    return b