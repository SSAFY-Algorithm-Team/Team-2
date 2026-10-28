def solution(info, edges):
    n = len(info)
    children = [[] for _ in range(n)]
    for p, c in edges:
        children[p].append(c)

    seen = {1}
    stack = [(1, 1, 0)]
    answer = 0
    while stack:
        mask, sheep, wolf = stack.pop()
        answer = max(answer, sheep)
        for node in range(n):
            if not mask & (1 << node):
                continue
            for child in children[node]:
                nxt = mask | (1 << child)
                if nxt == mask or nxt in seen:
                    continue
                if info[child] == 0:
                    seen.add(nxt)
                    stack.append((nxt, sheep + 1, wolf))
                elif sheep > wolf + 1:
                    seen.add(nxt)
                    stack.append((nxt, sheep, wolf + 1))
    return answer
