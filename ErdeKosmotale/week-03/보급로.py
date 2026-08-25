#SWEA D4 보급로

#다익스트라 알고리즘, BFS 등으로 풀이가 가능하였음.

#출발지와 도착지가 지정되어 있을때 다익스트라 알고리즘을 떠올려볼수 있었으면.......

import heapq

def dijkstra(lst):

    INF=float('inf')
    pq=[] #거리,row,col
    n=len(lst)

    distances=[[INF]*n for _ in range(n)]    
    direction=[(-1,0),(1,0),(0,-1),(0,1)]

    heapq.heappush(pq,(0,0,0)) #거리, row, col
    
    while pq:

        distance,row,col=heapq.heappop(pq)

        for r,c in direction:

            n_row=row+r
            n_col=col+c

            if(n_row<0 or n_row>=n or n_col<0 or n_col>=n):
                continue

            # if(n_row==n-1 and n_col==n-1):
            #     return distances[n-1][n-1]

            if(distances[n_row][n_col]>distance+lst[n_row][n_col]):
                heapq.heappush(pq,(distance+lst[n_row][n_col],n_row,n_col))
                distances[n_row][n_col]=distance+lst[n_row][n_col]

    return distances
        
        
T = int(input())

for test_case in range(1, T + 1):
    
    n=int(input())
    lst=[list(map(int,input())) for _ in range(n)]

    distances=dijkstra(lst)

    print(f"#{test_case} {distances[n-1][n-1]}")