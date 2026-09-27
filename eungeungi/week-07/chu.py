import math

def chu(N, weights):
    visited = [False] * N
    result = 0
    total = sum(weights)

    def dfs(cnt, left, right, remain):
        nonlocal result

        if cnt == N:
            result += 1
            return
        # 남은 추는 rest
        # 남은 추 무게와 오른쪽 저울 무게 합쳐도 왼쪽보다 적은 경우 그 이후를 안 보고도 result에 미리 더하기
        # 3개가 남았다면 3! * (왼쪽, 오른쪽 2가지선택) 2^3 곱한것
        if left >= right + remain:
            rest = N - cnt
            result += math.factorial(rest) * (2 ** rest)
            return

        for i in range(N):
            if visited[i]:
                continue

            visited[i] = True
            w = weights[i]

            # 왼쪽
            dfs(cnt + 1, left + w, right, remain - w)

            # 오른쪽
            if right + w <= left:
                dfs(cnt + 1, left, right + w, remain - w)

            visited[i] = False

    dfs(0, 0, 0, total)

    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))

    ans = chu(N, weights)

    print(f"#{tc} {ans}")