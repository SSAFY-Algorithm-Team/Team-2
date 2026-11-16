# 프로그래머스 부대복귀
# https://school.programmers.co.kr/learn/courses/30/lessons/132266?language=python3
# bfs 풀이

from collections import deque


def solution(n, roads, sources, destination):
    """
    반대로 생각하기!
    destination에서 bfs를 돌려 모든 노드까지의 최단거리 찾기 
    - 초기화 값 -1 => 도달 못하는 값 처리
    - destination은 0으로 시작 => 출발지와 도착지가 같은 경우 처리
    마지막에 source 기준으로 거리값 출력
    """

    # 그래프 만들기
    graph = {i: [] for i in range(1, n + 1)}
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # destination에서 출발해서 모든 노드에 도달하는 최소 거리 구하기
    queue = deque([(destination, 0)])
    dist = [-1] * (n + 1)
    dist[destination] = 0

    while queue:
        node, curr = queue.popleft()

        for next_n in graph[node]:
            if dist[next_n] == -1:
                queue.append((next_n, curr + 1))
                dist[next_n] = curr + 1

    # source에 맞는 값만 출력
    result = []
    for s in sources:
        result.append(dist[s])
    
    return result


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))



