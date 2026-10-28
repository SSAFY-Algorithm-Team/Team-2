import heapq

def dijkstra(graph,start,k,n):
    
    distances = [(10**10)] * (n+1)
    heap = [(0,start)]
    distances[start] = 0
    
    while heap:
        
        dist, node_now = heapq.heappop(heap)
        
        if(dist > distances[node_now]):
            continue
        
        for node, weight in graph[node_now]:
            
            new_distance = dist + weight
            if(new_distance < distances[node]):
                
                distances[node] = new_distance
                heapq.heappush(heap,(new_distance,node))
        
    return distances[k]    


def solution(n, s, a, b, fares):
    
    graph =[[] for _ in range(n+1)]
    
    for u, v , w in fares:
        
        graph[u].append((v,w))
        graph[v].append((u,w))  #s와 e 사이 간선 연결
        
    answer = 10**10
    
    for i in range(1,n+1):
        
        answer_temp = 0
        
        wit = dijkstra(graph,s,i,n)
        a_dist   = dijkstra(graph,i,a,n)
        b_dist   = dijkstra(graph,i,b,n)
        
        print(wit,a_dist,b_dist)
        
        answer_temp += (wit+a_dist+b_dist)
    
        answer = min(answer,answer_temp)
    
    return answer
        