# 프로그래머스 등산코스 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118669?language=python3
# 아 어려워....

import heapq

def solution(n, paths, gates, summits):

    # 그래프 만들기
    graph = {i: [] for i in range(1, n + 1)}
    for i, j, w in paths:
        graph[i].append((j, w)) # 시작노드 : [(끝 노드, 가중치), (끝 노드, 가중치), ...]
        graph[j].append((i, w))

    candi = []
    dist = [10000001] * (n + 1)
    for gate in gates:
        heapq.heappush(candi, [0, gate]) # intensity(계속 최소 intensity를 유지하며 쓸거임), 시작 노드
        dist[gate] = 0


    while candi:
        intensity, node = heapq.heappop(candi)

        # 이 node가 다른 gates를 지난다면 조건에 안맞음 => ??
        # 이 intensity 지금까지 발견된 최소 intensity보다 크다면 조사할 필요 없음
        if intensity > dist[node]: 
            continue

        if node in summits:
            dist[node] = intensity
            continue

        for nxt_n, nxt_w in graph[node]:
            n_intense = max(intensity, nxt_w) # nxt_w가 더 크다면 intensity가 업데이트 돼야함 (intensity는 항상 그 경로에서 최대값 유지)
            if n_intense < dist[nxt_n]:
                dist[nxt_n] = n_intense
                heapq.heappush(candi, [n_intense, nxt_n])

    # 모은 dist들로 최소 intensity랑 그 때 봉우리가 뭔지 구함
    min_intensity = 10000001
    best_summit = n
    for summit in summits:
        if dist[summit] < min_intensity:
            min_intensity = dist[summit]
            best_summit = summit
        elif dist[summit] == min_intensity:
            best_summit = min(summit, best_summit)

    return best_summit, min_intensity


ans = solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
print(ans)

