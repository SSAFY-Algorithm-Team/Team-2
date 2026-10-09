from collections import deque

def bfs():

    numbers[N] = 1


    while(queue):
        n, cnt = queue.popleft()
    
    
        
        if(n==M):
            return cnt
    
        if(n*2 <= 1000000 and not numbers[n*2]):
            numbers[n*2]= 1
            queue.append((n*2, cnt+1))
    
        if(n+1<= 1000000 and not numbers[n+1]):
            numbers[n+1] = 1
            queue.append((n+1, cnt+1))
    
        if(n-1>0 and not numbers[n-1]):
            numbers[n-1] = 1
            queue.append((n-1,cnt+1))
    
        if(n-10>0 and not numbers[n-10]):
            numbers[n-10] = 1
            queue.append((n-10, cnt + 1))

T = int(input())


for test_case in range(1, T + 1):

    N , M = map(int,input().split())

    numbers = [0] * (1000000)

    queue = deque()
    queue.append((N,0))

    ans = dfs()

    print(f"#{test_case} {ans}")

