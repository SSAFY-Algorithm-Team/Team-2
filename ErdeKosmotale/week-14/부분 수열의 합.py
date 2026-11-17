
T = int(input())

def dfs(idx,now_num):

    global answer

    if(now_num > K):
        return
    
    if(idx == N):
        
        if(now_num==K):
            answer += 1
        return

    dfs(idx+1 , now_num + lst[idx])
    dfs(idx+1 , now_num )

for test_case in range(1,T + 1):

    N , K = map(int,input().split())
    lst = list(map(int,input().split()))
    answer = 0

    dfs(0,0)

    print(f"#{test_case} {answer}")

    

        
    
    