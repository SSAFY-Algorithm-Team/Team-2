

def dfs(tree_parent,idx):

    global ans

    ans+=1
        
        
    for idx_new in tree_parent[idx]:

        dfs(tree_parent,idx_new)
        

T = int(input())

for test_case in range(1, T + 1):

    ans=0

    E,N=map(int,input().split())

    lst_cmd=list(map(int,input().split()))

    lst_parent=[[] for _ in range(E+2)]
    
    for i in range(0,2*E,2):

        
        idx_parent=lst_cmd[i]
        idx_child= lst_cmd[i+1]

        lst_parent[idx_parent].append(idx_child)

    
    dfs(lst_parent,N)

    print(f"#{test_case} {ans}")
        