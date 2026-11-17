import sys
sys.setrecursionlimit(10**9)

def solution(n,computers):
    
    parent = list(range(n+1))
    
    def find(x):
        
        if(parent[x] != x):
            parent[x] = find(parent[x])
            
        return parent[x]
    
    def union(x,y):
        
        x = find(x)
        y = find(y)
        
        if(x != y):
            
            parent[y] = x
            
    for i in range(len(computers)):
        
        first = i + 1
        
        for j in range(len(computers[i])):
            
            second = j + 1 
            
            if(computers[i][j] == 1):
                union(first,second)
    
    print(parent)
    
    #ans = len({find(i) for i in range(1, n + 1)})
    
    ans = len({find(i) for i in range(1,n+1)})
    
    
    
   
    return ans
            
# def solution(n, computers):
#     answer = 0
    
#     graph=[[] for _ in range(n)] #0번부터 n-1까지
    
#     for node in range(len(computers)):
        
#         for i_node in range(len(computers[node])):
            
#             if(node==i_node):
#                 continue
            
#             if(computers[node][i_node]==1):
#                 graph[node].append(i_node)
    
#     visited=[0]*n
    
#     def dfs(lst,node):
        
#         visited[node]=1
        
#         for i in lst[node]:
#             if(visited[i]==0):
#                 dfs(lst,i)
        
#         return
    
#     for i in range(n):
#         if(visited[i]==0):
#             answer+=1
#             dfs(graph,i)
    
#     return answer