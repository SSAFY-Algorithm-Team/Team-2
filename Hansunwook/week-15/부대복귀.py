from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    # 문제 이해하는데 너무 오래걸림...
    # 그니까 각 길을 가는데 1만큼 걸리는 거고
    # 각 위치가 연결되어 있는데 각 부대원의 위치가 나왔을 때 destination로 가는 길이를 구하는 건가
    # 그러면 각 부대원별로 구하기 보다는 강철부대에서 시작해서 bfs로 거리를 업데이트 하면서 구하고 마지막에 
    # 각 부대원의 거리를 출력하면 될듯?
    
    #일단 먼저 bfs 하기 위한 인접 리스트 만들기
    arr = []
    for i in range(n+1):
        arr.append([])
    # print(arr)
    for a,b in roads:
        arr[a].append(b)
        arr[b].append(a)
    # print(arr)
    
    #bfs
    dis = [-1]*(n+1)
    que = deque([destination])
    dis[destination] = 0
    while(que):
        now = que.popleft()
        for next in arr[now]:
            if dis[next] == -1:
                dis[next] = dis[now] + 1
                que.append(next)
    for i in sources:
        answer.append(dis[i])
    return answer