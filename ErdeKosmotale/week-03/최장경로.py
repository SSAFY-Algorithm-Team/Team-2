#swea D3 최장경로

#인접 리스트 형태의 그래프를 백트래킹 탐색하는 법을 생각해볼 것

def dfs(graph,node,visited,k):
    global ans
    ans=max(ans,k)
    visited[node]=True

    for node_new in graph[node]:

        if(visited[node_new]==False):
            visited[node_new]=True
            dfs(graph,node_new,visited,k+1)
            visited[node_new]=False

    return
    
T=int(input())

for test_case in range(1,T+1):

    n,m=map(int,input().split())

    graph=[list() for _ in range(n)]

    for _ in range(m):
        x,y=map(int,input().split())

        x-=1
        y-=1

        graph[x].append(y)
        graph[y].append(x)

    ans=0

    for i in range(n):
        visited=[False]*n
        dfs(graph,i,visited,1)

    print(f"#{test_case} {ans}")