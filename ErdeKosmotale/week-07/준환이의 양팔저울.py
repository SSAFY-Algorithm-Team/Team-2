
T = int(input())

def dfs(lst,idx,left,right):

    global ans
    
    if(right>left):
        return

    if(2*left>sum_weight):

        ans += (2**(N-idx))
        return

    if(idx==N):
        
        ans+=1

        return

    dfs(lst,idx+1, left + lst[idx] , right)

    if(right+lst[idx]>sum_weight):
        return

    else:
        dfs(lst,idx+1, left , right + lst[idx])

    return

def permutation():

    path=[]
    used=[0]*N

    def backtrack():

        if(len(path)==N):

            dfs(path[:],1,path[0],0)
            
            return
        
        for i in range(N):

            if(used[i]==False):
                path.append(lst_weight[i])
                used[i]=True
                backtrack()
                used[i]=False
                path.pop()

    backtrack()

for test_case in range(1,T+1):
    ans=0

    N = int(input())

    lst_weight = list(map(int,input().split()))

    sum_weight= sum(lst_weight)

    permutation()

    print(f"#{test_case} {ans}")

    