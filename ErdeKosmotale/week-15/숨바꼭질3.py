import heapq

MAX = 100000
INF = float('inf')

N, K = map(int, input().split())

dist = [INF] * (MAX + 1)
dist[N] = 0
pq = [(0, N)]   # (걸린 시간, 위치)

while pq:
    cost, now = heapq.heappop(pq)

    if cost > dist[now]:      # 이미 더 짧은 길로 처리된 위치면 건너뛰기
        continue
    if now == K:             
        break

    for nxt, w in ((now * 2, 0), (now - 1, 1), (now + 1, 1)):
        if 0 <= nxt <= MAX and cost + w < dist[nxt]:
            dist[nxt] = cost + w
            heapq.heappush(pq, (cost + w, nxt))

print(dist[K])


# 시간초과 난 코드
# from collections import deque 

# ##음?

# def bfs():

#     global ans

#     queue = deque()
#     queue.append((N,0))

#     visited = {}

#     while(queue):

#         now, t = queue.popleft()

#         if(now == K):
#             ans = t
#             return 

#         if(now+1 not in visited or visited[now+1] > t+1): 
#             queue.append((now+1,t+1))
#             visited[now+1] = t + 1
        
#         if(now-1 not in visited or visited[now-1] > t+1):

#             queue.append((now-1,t+1))
#             visited[now-1] = t + 1

#         if(now*2 not in visited or visited[now*2]>t):
#             queue.append((now*2,t))
#             visited[now*2] = t
#     return
        
        
# N, K = map(int,input().split())

# ans= 0

# bfs()

# print(ans)