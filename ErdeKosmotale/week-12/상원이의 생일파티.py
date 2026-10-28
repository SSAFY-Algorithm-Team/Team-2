from collections import deque

T = int(input())

for test_case in range(1, T + 1):

    N , M = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N + 1)
    for _ in range(M):

        a,b = map(int,input().split())

        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append((1,0))

    visited[1] = True

    ans = -1
    while(queue):

        node, dist = queue.popleft()

        if(dist<=2):
            ans +=1

        if(dist>2):
            break
        
        for node_new in graph[node]:

            if(not visited[node_new]):
                queue.append((node_new,dist+1))
                visited[node_new] = True


    print(f"#{test_case} {ans}")