def comb2(comb1):
    path=[]
    ans2=0
    def backtrack(idx,weight,ans_inter):
        nonlocal ans2
        
        if(idx==M):

            ans2=max(ans2,ans_inter)
            return
        if(weight+comb1[idx]<=L):
            
            backtrack(idx+1,weight+comb1[idx],ans_inter+comb1[idx]**2)

        backtrack(idx+1,weight,ans_inter)

    backtrack(0,0,0)

    return ans2

        # if(weight>L or len(path)>M):
        #     return

        # for i in range(start,M):
        #     if(weight+comb1[i]<=L):
        #         path.append(i)
        #         backtrack(i+1,weight+comb1[i],ans_inter+weight**2)
                


def combination():
    ans=0
    path=[]
    visited=[0]*(N*N)
    def backtrack(start):
        nonlocal ans
        if(len(path)==2):
            ans_inter=0
            
            for row in path:
                print(row)
                ans_inter+=comb2(row)

            ans=max(ans,ans_inter)
            return

        for i in range(start,N*N-M+1):

            if(not visited[i]):
                path.append(lst[i:i+M])
                for j in range(i,i+M):
                    visited[j]=True
                backtrack(start+M)
                for j in range(i,i+M):
                    visited[j]=False
                path.pop()
        
                    
    backtrack(0)

    return ans  
                    

T=int(input())

for test_case in range(1,T+1):

    N,M,L= map(int,input().split())

    lst=[]

    for _ in range(N):

        lst += list(map(int,input().split())) 

    ans=combination()

    print(ans)

