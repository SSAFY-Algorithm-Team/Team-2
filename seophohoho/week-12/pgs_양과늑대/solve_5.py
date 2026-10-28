def solution(info, edges):
    n = len(info)
    parent = [-1] * n
    for p, c in edges:
        parent[c] = p

    reachable = [False] * (1 << n)
    reachable[1] = True
    answer = 1
    for mask in range(3, 1 << n, 2):
        sheep = wolf = 0
        for v in range(n):
            if mask & (1 << v):
                if info[v] == 0:
                    sheep += 1
                else:
                    wolf += 1
        if sheep <= wolf:
            continue
        for v in range(1, n):
            if mask & (1 << v) and mask & (1 << parent[v]) and reachable[mask ^ (1 << v)]:
                reachable[mask] = True
                answer = max(answer, sheep)
                break
    return answer
