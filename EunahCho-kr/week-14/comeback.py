import heapq

def solution(n, roads, sources, destination):
    # 그래프 만들기 (양방향, 인접)
    graph = {v : [] for v in range(1, n + 1)}
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)


    # 그래프에 있는 노드 값들이 1-based -> 사용하는 모든 변수를 1-based로 맞추기
    dist = [float('inf')] * (n + 1) # 각 노드에서 destination까지 최단거리 -> 나중에 병사들의 노드에 적혀있는 최단거리만 구하면 됨

    heap = []
    heapq.heappush(heap, (0, destination)) 
    dist[destination] = 0

    while heap:
        curr, node = heapq.heappop(heap) # 이 노드가 온 거리, i번쩨 군인(1-based), 지금 탐색 노드

        ## 나온 노드가 sources 안에 있으면 탐색 종료 하려고 했는데 안됨 --> 왜지

        for next in graph[node]:
            if curr + 1 < dist[next]:  # 다음 행선지에 도착하는 거리가 dist에 저장된 값보다 작을 때만 사용 -> 이 과정에서 사이클 정리 / 가지치기
                dist[next] = curr + 1
                heapq.heappush(heap, (curr + 1, next))

    result = []
    for s in sources:
        if dist[s] == float('inf'):
            result.append(-1)
        else:
            result.append(dist[s])
        
    return result


# print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
"""
- 21번째 줄
- 왜 출발지 시작은 안되고 도착지 시작은 되는지
- dist 차원 결정 -> 한 리스트로만 해도 됐던 이유?
- BFS 코드도 고쳐서 써보기 + 다익스트라랑 시간 차이 비교
- 이거도 보충수업 깃랩에 올리기
"""

############################# BFS 코드 -> 시간초과

# from collections import deque

# def solution(n, roads, sources, destination):
#     # 그래프 만들기 (양방향, 인접)
#     graph = {v : [] for v in range(1, n + 1)}
#     for u, v in roads:
#         graph[u].append(v)
#         graph[v].append(u)


#     # 그래프에 있는 노드 값들이 1-based -> 사용하는 모든 변수를 1-based로 맞추기
#     num = len(sources) # 군인 몇 명인지
#     dist = [[float('inf')] * (num + 1) for _ in range(n + 1)] # row번째 지역을 col번째 군인이 얼마나 걸려서 도착했는지 메모 (단, 항상 최단거리로 유지)
#     result = [-1] * (num + 1) # 최종 결과 값 반환용 -> i번째 군인이 목적지 도착까지 얼마나 걸렸는지

#     queue = deque()
#     for i, s in enumerate(sources):
#         queue.append((i + 1, s, 0)) # i번째 군인, s노드에서 시작, 누적 거리 0 

#     while queue:
#         i, node, curr = queue.popleft() # i번쩨 군인(1-based), 지금 탐색 노드, 이 노드가 온 거리

#         # destination에 해당하는 노드에 도달하면 i번째 군인은 탐색 종료
#         if node == destination:
#             final = dist[node][i]
#             # dist값이 한 번도 업데이트 되지 않고 destination에 도착했다 -> destination이 출발지였다
#             if final == float('inf'):
#                 final = 0
#             result[i] = final 
#             # result[i] = curr 값으로 사용해도 되나? 더 생각 
#             # -> bfs에선 지금 나온 curr값이 그 노드에 도달하는 최소값인걸 보장 못함 
#             # -> 다익스트라면 보장하므로 curr써도 된다? => 검증 받기
#             continue

#         for next in graph[node]:
#             if curr + 1 < dist[next][i]: # i번째 군인이 다음 행선지에 도착하는 거리가 dist에 저장된 값보다 작을 때만 사용
#                                         # 이 과정에서 사이클 정리 / 가지치기 된다고 생각했는데 시간초과 --> 추가 가지치기? 다익스트라?                   
#                 dist[next][i] = curr + 1 
#                 queue.append((i, next, curr + 1))

#     return result[1:]