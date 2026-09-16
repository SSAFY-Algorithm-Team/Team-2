
T=int(input())


for test_case in range(1,T+1):

    lst_cmd= list(map(int,input().split()))

    n_node=lst_cmd[0]

    graph=[]

    
    for i in range(1,len(lst_cmd),n_node):

        t=lst_cmd[i:i+n_node]
        graph.append(t[:])

    for row in range(n_node):
        for col in range(n_node):
            if(row==col):
                continue

            if(graph[row][col]==0):
                graph[row][col]=1500

        
    for k in range(n_node):
        for i in range(n_node):
            for j in range(n_node):

                if(graph[i][j]>graph[i][k] + graph[k][j]):
                    graph[i][j]=graph[i][k]+graph[k][j]

    ans=10**9
    for row in graph:
        ans_inter=sum(row)
        ans=min(ans,ans_inter)

    print(f"#{test_case} {ans}")
        