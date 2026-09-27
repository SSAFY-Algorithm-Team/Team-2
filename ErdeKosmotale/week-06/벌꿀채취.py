def comb2(comb1):
<<<<<<< HEAD
    path=[]
    ans2=0
    def backtrack(idx,weight,ans_inter):
        nonlocal ans2
        
        if(idx==M):

            ans2=max(ans2,ans_inter)
            return
        if(weight+comb1[idx]<=L):
            
            backtrack(idx+1,weight+comb1[idx],ans_inter+comb1[idx]**2)

=======
    ans2=0
    def backtrack(idx,weight,ans_inter):
        nonlocal ans2

        if(weight>L):
            return
        
        if(idx==M):
            
            ans2=max(ans2,ans_inter)
            return
        
        backtrack(idx+1,weight+comb1[idx],ans_inter+comb1[idx]**2)            
>>>>>>> 3388efed2279e02c501aa484157b84c6c38742ba
        backtrack(idx+1,weight,ans_inter)

    backtrack(0,0,0)

    return ans2

<<<<<<< HEAD
        # if(weight>L or len(path)>M):
        #     return

        # for i in range(start,M):
        #     if(weight+comb1[i]<=L):
        #         path.append(i)
        #         backtrack(i+1,weight+comb1[i],ans_inter+weight**2)
                


=======
                

>>>>>>> 3388efed2279e02c501aa484157b84c6c38742ba
def combination():
    ans=0
    path=[]
    visited=[0]*(N*N)
    def backtrack(start):
        nonlocal ans
        if(len(path)==2):
<<<<<<< HEAD
            ans_inter=0
            
            for row in path:
                print(row)
                ans_inter+=comb2(row)

            ans=max(ans,ans_inter)
=======

            ans_inter=0
            
            for row in path:
                
                ans_inter+=comb2(row)

            ans=max(ans,ans_inter)

>>>>>>> 3388efed2279e02c501aa484157b84c6c38742ba
            return

        for i in range(start,N*N-M+1):

<<<<<<< HEAD
            if(not visited[i]):
                path.append(lst[i:i+M])
                for j in range(i,i+M):
                    visited[j]=True
                backtrack(start+M)
                for j in range(i,i+M):
                    visited[j]=False
=======
            if(i % N + M <= N):
                path.append(lst[i:i+M])
                backtrack(i+M)
>>>>>>> 3388efed2279e02c501aa484157b84c6c38742ba
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

<<<<<<< HEAD
    print(ans)
=======
    print(f"#{test_case} {ans}")
>>>>>>> 3388efed2279e02c501aa484157b84c6c38742ba

