# 13549 숨바꼭질 3 골드5
# https://acmicpc.net/problem/13549


"""
수빈 N 동생 K
수빈 X + 1, X - 1 (1초), 2 * X (0초)

수빈이 동생을 찾는 가장 빠른 시간
"""

N, K = map(int, input().split())

DP = [0] * 100001  # i번째 위치까지 수빈이가 이동한 시간

# N보다 이전은 1초씩 걸려서 가는 방법뿐
for i in range(N - 1, -1, -1):
    DP[i] = N - i

# N보다 이후는 1초씩 걸리거나, 순간이동 할 수 있음
for i in range(N + 1, 100001):
    if i % 2 == 0:
        DP[i] = min(DP[i-1] + 1, DP[i//2])
    else:
        DP[i] = DP[i-1] + 1

print(DP[:20])
print(DP[K])
