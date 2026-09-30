from collections import defaultdict


def town(N, M, g):
    # 방문 확인
    visited = [False] * (N + 1)
    result = 0

    def dfs(person):
        visited[person] = True
        # value 확인
        for next_person in g[person]:
            if not visited[next_person]:
                dfs(next_person)

    for person in range(1, N + 1):
        if not visited[person]:
            dfs(person)
            result += 1

    return result


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    g = defaultdict(list)

    for _ in range(M):
        a, b = map(int, input().split())

        g[a].append(b)
        g[b].append(a)

    ans = town(N, M, g)

    print(f"#{tc} {ans}")