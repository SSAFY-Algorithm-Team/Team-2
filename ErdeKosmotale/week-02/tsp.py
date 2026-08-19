INF=float('inf')

def cal_distance(graph,i,j):

    x=abs(graph[i][0]-graph[j][0])
    y=abs(graph[i][1]-graph[j][1])

    return x+y

def tsp(i,visited,graph,n_node,dp):

    if(visited==(1<<(n_node-1))-1): 
        return cal_distance(graph,i,n_node-1) if cal_distance(graph,i,n_node-1) else INF

    if(dp[i][visited]!=-1):
        return dp[i][visited]

    

    dp[i][visited]=INF
    for j in range(n_node-1):
        if(visited & (1<<j)):
            continue
        dp[i][visited]=min(dp[i][visited],cal_distance(graph,i,j)+tsp(j,(visited|(1<<j)),graph,n_node,dp))    

    return dp[i][visited]
    
T=int(input())

for test_case in range(1,T+1):

    n=int(input())
    lst=list(map(int,input().split()))

    graph=[]

    for i in range(0,len(lst),2):
        if(i==2):
            continue
        graph.append((lst[i],lst[i+1]))

    graph.append((lst[2],lst[3]))
    n_node=len(graph)

    dp=[[-1]*(1<<(n_node-1)) for _ in range(n_node-1)]
    
    ans=(tsp(0,1,graph,n_node,dp))

    print(f"#{test_case} {ans}")