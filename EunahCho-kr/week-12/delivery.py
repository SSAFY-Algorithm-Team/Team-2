# 프로그래머스 배달
# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq

def solution(N, road, K):
    
    graph = [[] for _ in range(N + 1)]
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w)) ## 필요한지 아닌지 헷갈려...

    dist = [20000001] * (N + 1)
    dist[1] = 0

    candidate = []
    heapq.heappush(candidate, [0, 1]) # [출발지 ~ 목적지 거리, 현재 위치]

    while candidate:
        acc, curr = heapq.heappop(candidate) # 지금까지 누적 거리, 현재 위치

        if dist[curr] < acc:
            continue

        for next, weight in graph[curr]:
            cost = acc + weight

            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(candidate, [cost, next])

    # print(dist)

    answer = 0
    for d in dist:
        if d <= K:
            answer += 1

    return answer


ans = solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
print(ans)


####### 강사님 코드랑 비교
# import heapq


# def dijkstra(start):
#     '''
#         start 정점에서부터 각 노드들까지 가는 최단경로
#         즉, 가중치 누적을 저장한 리스트를 반환
#     '''

#     # 비교하며 최소값을 업데이트 할 것이기에, 충분히 큰 숫자가 초기값이어야함
#     distance = {v: float('inf') for v in graph}
#     distance[start] = 0  # 시작 지점까지 도달하는 비용은 0
#     candidate = []  # 최소힙 후보군
#     # 가중치를 기준으로 최소힙 [가중치, 현재위치]
#     heapq.heappush(candidate, [0, start])

#     while candidate:  # 후보군이 있으면 조사
#         acc_curr, curr = heapq.heappop(candidate)
#         # 후보군으로부터 얻어낸 현재 위치는 반드시 조사하나?
#         # -> 아님. 이전에 이미 지금까지 누적된 값보다 더 싸게 도착한 적이 있다면 무시
#         if distance[curr] < acc_curr: continue
#         # 조사할 가치가 충분하다면, 현재 위치에서 다시 후보군 탐색
#         for next_v, weight in graph[curr].items():
#             # curr 위치에서 next_v로 가는데 드는 누적 비용을 계산
#             cost = acc_curr + weight
#             # 이 코스트 역시 다음 위치로 가볼만 한가?
#             if distance[next_v] > cost:
#                 distance[next_v] = cost
#                 heapq.heappush(candidate, [cost, next_v])

#     return distance


# graph = {
#     'a': {'b': 3, 'c': 5},
#     'b': {'c': 2, 'd': 6},
#     'c': {'b': 1, 'd': 4, 'e': 6},
#     # 'c': {'b': -4, 'd': 4, 'e': 6}, # 다익스트라는 가중치에 음수가 있으면 안됨 (저 끝까지 내려가버림)
#     'd': {'e': 2, 'f': 3},
#     'e': {'a': 3, 'f': 6},
#     'f': {}
# }
# start_v = 'a'
# res = dijkstra(start_v)
# print(res)  # {'a': 0, 'b': 3, 'c': 5, 'd': 9, 'e': 11, 'f': 12}