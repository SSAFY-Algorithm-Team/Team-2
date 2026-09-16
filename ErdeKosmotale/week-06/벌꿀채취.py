def comb2(comb1):
    ans2=0
    def backtrack(idx,weight,ans_inter):
        nonlocal ans2

        if(weight>L):
            return
        
        if(idx==M):
            
            ans2=max(ans2,ans_inter)
            return
        
        backtrack(idx+1,weight+comb1[idx],ans_inter+comb1[idx]**2)            
        backtrack(idx+1,weight,ans_inter)

    backtrack(0,0,0)

    return ans2

                

def combination():
    ans=0
    path=[]
    visited=[0]*(N*N)
    def backtrack(start):
        nonlocal ans
        if(len(path)==2):

            ans_inter=0
            
            for row in path:
                
                ans_inter+=comb2(row)

            ans=max(ans,ans_inter)

            return

        for i in range(start,N*N-M+1):

            if(i % N + M <= N):
                path.append(lst[i:i+M])
                backtrack(i+M)
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

    print(f"#{test_case} {ans}")

