# N,K = map(int,input().split())
# 순간이동은 비용이 들지 않으니까 최대한 순간이동을 하는 쪽으로 해야 한다
# +-1 or *2 셋중 하나
# 음음 그때마다 3중 하나니까 dfs나 bfs로 세개중 하나를 고르기 시키면 

#근데 *2가 무조건 이득이라 최대한 써야 하는데..
#그러면 각 턴마다 -1 / +1 / 0인지 고르고 *2 할지말지 고르게 한다면?
#일단 bfs는 생각 안나니까 bfs로 시작

# move = [0,-1,1]
# move_skip = [1,2]
# visit = []
# for i in range(2):
#     visit.append([False]*3)
# result = [0]
# min_result = [100000]
# def dfs(val,count):
#     if val > K:
#         return
#     if val == K:
#         if count < min_result[0]:
#             min_result[0] = count
#         return 
#     for i in range(3):
#         for j in range(2):
#             if visit[i][j]:
#                 continue
#             if i == 0:
#                 visit[i][j] = True
#                 dfs(val*move_skip[j],count)
#                 visit[i][j] = False
#             else:
#                 visit[i][j] = True
#                 dfs((val+move[i])*move_skip[j],count+1)
#                 visit[i][j] = False

# if K % N != 0:
#     dfs(N,0)
# else:
#     min_result[0] = 0

# print(min_result[0])

# dfs 재귀 깊이 너무 깊어짐 그럼 bfs로 하기
# bfs 구현
from collections import deque
N,K = map(int,input().split())
MAX = 100000
move = [-1,1]
visit = [False]*(MAX+1)

now = [N]
visit[N] = True
count = 0

while True:
    i = 0
    while i < len(now):
        x = now[i]
        i += 1
        nx = x * 2
        if 0 <= nx <= MAX and not visit[nx]:
            visit[nx] = True
            now.append(nx)

    if K in now:
        print(count)
        break

    nxt = []
    for x in now:
        for d in move:
            nx = x + d
            if 0 <= nx <= MAX and not visit[nx]:
                visit[nx] = True
                nxt.append(nx)
    now = nxt
    count += 1
