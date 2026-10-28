import heapq

def solution(N, road, K):
    # 1. 그래프 만들기 (양방향)
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 2. 다익스트라
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]  # (지금까지 걸린 시간, 마을)

    while pq:
        cost, now = heapq.heappop(pq)
        if cost > dist[now]:      # 이미 더 짧은 길로 처리된 마을이면 건너뜀
            continue
        for nxt, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    # 3. K 이하인 마을 세기
    return sum(1 for d in dist[1:] if d <= K)
