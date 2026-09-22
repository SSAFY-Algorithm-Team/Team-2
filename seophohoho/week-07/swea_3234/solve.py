import math

T = int(input())

def dfs(used, left, right, remain_sum, remain_cnt):
    if remain_cnt == 0:
        return 1
    if left >= right + remain_sum:
        return math.factorial(remain_cnt) * (1 << remain_cnt)
    count = 0
    for i in range(N):
        if used & (1 << i):
            continue
        w = weights[i]
        nxt = used | (1 << i)
        count += dfs(nxt, left + w, right, remain_sum - w, remain_cnt - 1)
        if left >= right + w:
            count += dfs(nxt, left, right + w, remain_sum - w, remain_cnt - 1)
    return count


for tc in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    print(f'#{tc} {dfs(0, 0, 0, sum(weights), N)}')
