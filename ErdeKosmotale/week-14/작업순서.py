from collections import deque

T = 10


for test_case in range( 1, T + 1):

    V, E = map(int,input().split())

    graph = [ [] for _ in range(V+1)]

    indegree = [0] * (V + 1)

    lst = list(map(int,input().split()))

    for i in range(0,len(lst),2):

        first = lst[i]
        second = lst[i+1]

        graph[first].append(second)
        indegree[second] += 1

    result = []

    queue = deque()

    for i in range(1,V+1):

        if(indegree[i] == 0):
            queue.append(i)


    while queue:

        now = queue.popleft()
        result.append(now)

        for i in graph[now]:

            indegree[i] -= 1

            if(indegree[i] == 0):
                queue.append(i)


    print(f"#{test_case}", end = ' ')

    for i in result:
        print(i,end=' ')

    print()
    
    
        
