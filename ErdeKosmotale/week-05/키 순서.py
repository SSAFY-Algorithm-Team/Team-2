from collections import deque

# 1번이 5번보다 작으면 화살표 1 -> 5

# (1 5 3) 얘네는? 4 (2 6) 얘네는?

# 하나 정점 확인하려면 graph_a에서 끝까지 탐색하고
# 나머지 정점         graph_b에서 끝까지 탐색했을 때 모든 노드를 다 포함하면
# 순위가 정해짐

def bfs(graph,node): #n번 노드에 대해!

    visited[node]=True

    n_visit=1

    queue=deque()
    queue.append(node)

    while(queue):
        node_now=queue.popleft()

        for next_node in graph.get(node_now,[]):
            if(not visited[next_node]):
                n_visit+=1
                visited[next_node]=True
                queue.append(next_node)

    return n_visit

T=int(input())

for test_case in range(1,T+1):

    N=int(input())
    M=int(input())

    graph={i:[] for i in range(1,N+1)}

    graph_b={i:[] for i in range(1,N+1)}

    for i in range(M):
        a,b=map(int,input().split())

        graph[a].append(b) #a보다 b가 작다는 뜻

        graph_b[b].append(a) #b보다 작은 노드 나타내기 위함

    ans=0
    for node in range(1,N+1):
        visited=[False]*(N+1)
        if((bfs(graph,node)+bfs(graph_b,node)-1)==N):
            
            ans+=1

    

    print(f"#{test_case} {ans}")

    

    
