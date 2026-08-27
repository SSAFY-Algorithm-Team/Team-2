# SWEA 2814 최장경로 (D3)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GOPPaAeMDFAXB&
# 시간 4h 30m / 시도 ?

def make_graph(n, lines):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = set()

    for line in lines:
        graph[line[0]].add(line[1])
        graph[line[1]].add(line[0])

    return graph


def solve(n, graph):
    visited = set()
    max_len = 0

    def dfs(depth, node):
        nonlocal max_len
        max_len = max(max_len, depth)
        # print("=" * 15)
        # print("depth : ", depth, "/ visited : ", visited)

        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                dfs(depth + 1, nxt)
                visited.remove(nxt)

    for start in range(1, n + 1):
        visited.add(start)
        dfs(1, start)
        visited.remove(start)

    return max_len


def main():
    T = int(input())
    for t in range(1, T+1):
        n, m = map(int, input().split())
        lines = [list(map(int, input().split())) for _ in range(m)]
        if lines:
            graph = make_graph(n, lines)
            ans = solve(n, graph)
            print(f"#{t} {ans}")
        else: # 예외 -> 간선 없으면 1 출력
            print(f"#{t} 1")


if __name__ == "__main__":
    main()


# ==== bfs 시도 -> 잘 안됨
# from collections import deque

# def bfs(n, m, lines):
#     is_used = [False] * m
#     queue = deque([(lines[0][0], lines[0][1], 2)]) # 정점 2개로 시작
#     is_used[0] = True
#     nodes = [0] * n

#     while queue:
#         print(queue)
#         print(nodes)
#         n1, n2, d = queue.popleft()
#         for idx in range(m):
#             nn1, nn2 = lines[idx]
#             if not is_used[idx]:
#                 if n1 == nn1 or n1 == nn2 or n2 == nn1 or n2 == nn2: # 더 효율적인 방법 없나?
#                     queue.append((nn1, nn2, d + 1))
#                     nodes[nn1 - 1] = d + 1
#                     nodes[nn2 - 1] = d + 1
#                     is_used[idx] = True
#     return max(nodes)

# === DFS
# 끝까지 못 간 경우 커버 못함
# 반대 방향으로 도는 경우 커버 못함
# def solve(n, m, lines):
#     is_used = [False] * 2
#     answer = 0
#     path = [lines[0]]
#     is_used[0] = True
#     def dfs(depth):
#         # print(depth, " / ", path)
#         nonlocal answer
#         if depth == m - 1:
#             # print("끝!")
#             tmp = set()
#             for p in path:
#                 tmp.update(p)
#             answer = len(tmp)
#             return 

#         for i in range(m):
#             if not is_used[i]:
#                 if  path[-1][-1] == lines[i][0]:
#                     path.append(lines[i])
#                     is_used[i] = True
#                     dfs(depth + 1)
#                     path.pop()
#                     is_used[i] = False
#     dfs(0)
#     return answer


# 이건 뭐지
# for i in range(m):
#     if not is_used[i]:
#         if  lines[i][0] == path[-1][-1] or lines[i][1] == path[-1][-1]:
#             path.append(lines[i])
#             is_used[i] = True
#             dfs(depth + 1)
#             path.pop()
#             is_used[i] = False

# 스택도 잘 안됨,, 
#     while stack:
#         val = stack.pop()
#         print("get out ", val)
#         if val not in visited:
#             if not path or val in graph[path[-1]]:
#                 visited.append(val)
#                 path.append(val)
#                 stack.extend(graph[val] - set(visited))
#                 dfs(depth + 1, val)
#                 max_len = max(max_len, len(set(path)))
#                 path.pop()
# for i in range(1, n+1) :
#     stack.append(i)
#     dfs(0, i)