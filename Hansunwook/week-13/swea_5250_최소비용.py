# from collections import deque
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     result = 0
#     N = int(input())
#     H = []
#     for i in range(N):
#         H.append(list(map(int,input().split())))

#     # 일단 dfs로 구현 후 다익스트라


#     #dfs
#     que = deque()
#     visit = []
#     for i in range(N):
#         visit.append([False]*N)
#     que.append([0,0,0])
#     disit = []
#     INF = float('inf')
#     for i in range(N):
#         disit.append([INF]*N)
#     udrl = [[0,1],[1,0],[-1,0],[0,-1]]
#     disit[0][0] = 0

#     while(que):
#         dis, nowa,nowb = que.popleft()
#         if dis > disit[nowa][nowb]:
#             continue
#         for i in range(4):
#             nexta = nowa + udrl[i][0]
#             nextb = nowb + udrl[i][1]
#             if 0 <= nexta < N and 0 <= nextb < N:
#                 nextdis = dis + 1
#                 if H[nowa][nowb] < H[nexta][nextb]:
#                     nextdis += H[nexta][nextb] - H[nowa][nowb]
#                 if disit[nexta][nextb] > nextdis:
#                     disit[nexta][nextb] = nextdis
#                     que.append((nextdis, nexta,nextb))
#     result = disit[N-1][N-1]

    
#     print(f"#{test_case} {result}")

import heapq
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    H = []
    for i in range(N):
        H.append(list(map(int,input().split())))

    # 일단 dfs로 구현 후 다익스트라


    #dfs
    que = [(0, 0, 0)]
    disit = []
    INF = float('inf')
    for i in range(N):
        disit.append([INF]*N)
    udrl = [[0,1],[1,0],[-1,0],[0,-1]]
    disit[0][0] = 0

    while(que):
        dis, nowa,nowb = heapq.heappop(que)
        if nowa == N-1 and nowb == N-1:
            result = dis
            break
        if dis > disit[nowa][nowb]:
            continue
        for i in range(4):
            nexta = nowa + udrl[i][0]
            nextb = nowb + udrl[i][1]
            if 0 <= nexta < N and 0 <= nextb < N:
                nextdis = dis + 1
                if H[nowa][nowb] < H[nexta][nextb]:
                    nextdis += H[nexta][nextb] - H[nowa][nowb]
                if disit[nexta][nextb] > nextdis:
                    disit[nexta][nextb] = nextdis
                    heapq.heappush(que, (nextdis, nexta, nextb))
    result = disit[N-1][N-1]

    
    print(f"#{test_case} {result}")