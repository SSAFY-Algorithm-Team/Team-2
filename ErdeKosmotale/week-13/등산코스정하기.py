import heapq

def solution(n, paths, gates, summits):
    
    graph = [[] for _ in range(n + 1)]
    
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    gate_set = set(gates)           # 나중에 조회 속도를 빠르게 하기 위해서 작성
    summit_set = set(summits)

    INF = float('inf')
    intensity = [INF] * (n + 1)
    heap = []

    
    for g in gates:
        intensity[g] = 0
        heapq.heappush(heap, (0, g))

    while heap:
        cur, node = heapq.heappop(heap)

        if cur > intensity[node]:
            continue
              
        if node in summit_set:             # 다른 산봉우리에는 접근하지 않음!
                                           # SET로 조회해서 속도가 좀 더 빠름
            continue

        for nxt, w in graph[node]:
            
            if nxt in gate_set:             # 다른 게이트로는 들어가지 않음!
                continue
            new = max(cur, w)   
            
            if new < intensity[nxt]:
                intensity[nxt] = new
                heapq.heappush(heap, (new, nxt))

    
    
    min_intensity = 10**9                        # 가장 작은 intensity가 포함된 산봉우리를 고르면 정답 ! 
    min_summit = 0
    
    print(intensity)
    for idx in range(1,len(intensity)):
        if(idx in summits):
            if(min_intensity> intensity[idx]):
                min_intensity = intensity[idx]
                min_summit = idx
    
    answer = [min_summit, min_intensity]
    return answer