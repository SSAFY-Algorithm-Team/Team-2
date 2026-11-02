from collections import deque
import heapq


T = int(input())

DIRECTION = [(-1,0),(1,0),(0,-1),(0,1)]

for test_case in range(1 , T+1):

    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]

    heap = [(0,0,0)]
    
    visited =[[10**9] * N for _ in range(N)]

    answer= 10**10

    while(heap):

        cost, c_row,c_col = heapq.heappop(heap)

        if(cost>=answer):
            continue
        
        if((c_row,c_col) == (N-1,N-1)):
            answer = min(answer,cost)

        for r , c in DIRECTION:

            n_row = c_row + r
            n_col = c_col + c

            if(0<=n_row<N and 0<=n_col<N):
                
                if(lst[n_row][n_col] > lst[c_row][c_col]):
                    now_cost = cost + 1 + (lst[n_row][n_col] - lst[c_row][c_col])

                else:
                    now_cost = cost + 1

                if(now_cost >= visited[n_row][n_col]):
                    continue

                if(now_cost < visited[n_row][n_col]):

                    heapq.heappush(heap,(now_cost,n_row,n_col))
                    visited[n_row][n_col] = now_cost

                
    print(f"#{test_case} {answer}")
                


        