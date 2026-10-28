def solution(info, edges):
    children = [[] for _ in range(len(info))]
    for p, c in edges:
        children[p].append(c)

    answer = 0

    def dfs(sheep, wolf, candidates):
        nonlocal answer
        answer = max(answer, sheep)
        for i, node in enumerate(candidates):
            rest = candidates[:i] + candidates[i + 1:] + children[node]
            if info[node] == 0:
                dfs(sheep + 1, wolf, rest)
            elif sheep > wolf + 1:
                dfs(sheep, wolf + 1, rest)

    dfs(1, 0, children[0])
    return answer
