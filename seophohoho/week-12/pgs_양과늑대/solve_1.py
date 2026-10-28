def solution(info, edges):
    n = len(info)
    children = [[] for _ in range(n)]
    for p, c in edges:
        children[p].append(c)

    seen = set()
    answer = 0

    def dfs(mask, sheep, wolf):
        nonlocal answer
        if mask in seen:
            return
        seen.add(mask)
        answer = max(answer, sheep)
        for node in range(n):
            if not mask & (1 << node):
                continue
            for child in children[node]:
                if mask & (1 << child):
                    continue
                if info[child] == 0:
                    dfs(mask | (1 << child), sheep + 1, wolf)
                elif sheep > wolf + 1:
                    dfs(mask | (1 << child), sheep, wolf + 1)

    dfs(1, 1, 0)
    return answer
