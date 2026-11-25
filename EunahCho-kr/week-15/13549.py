# 13549 숨바꼭질 3 골드5
# https://acmicpc.net/problem/13549


"""
수빈 N 동생 K
수빈 X + 1, X - 1 (1초), 2 * X (0초)

수빈이 동생을 찾는 가장 빠른 시간
"""

# 클로드
# i가 홀수면 i//2에서 바로 올 수 없지만, (i+1)//2 → i+1 → i로는 1초에 올 수 있어요. 
# 짝수 i는 i+1(홀수)이 순간이동 도착지가 될 수 없어서 이런 경우가 생기지 않아요. 그래서 홀수일 때 식만 고치면 돼요.

N, K = map(int, input().split())

DP = [0] * 100001

for i in range(N - 1, -1, -1):
    DP[i] = N - i

for i in range(N + 1, 100001):
    if i % 2 == 0:
        DP[i] = min(DP[i-1] + 1, DP[i//2])
    else:
        DP[i] = min(DP[i-1], DP[(i+1)//2]) + 1   # (i+1)//2 → i+1 → i 경로 추가

print(DP[K])


########################


# 지금 코드는 i로 올 때 i-1에서 걸어오거나 i//2에서 순간이동하는 경우만 봐요. 
# 그런데 순간이동으로 i+1까지 간 다음 1칸 뒤로 걷는 경로가 더 빠를 때가 있어요.

# N, K = map(int, input().split())

# DP = [0] * 100001  # i번째 위치까지 수빈이가 이동한 시간

# # N보다 이전은 1초씩 걸려서 가는 방법뿐
# for i in range(N - 1, -1, -1):
#     DP[i] = N - i

# # N보다 이후는 1초씩 걸리거나, 순간이동 할 수 있음
# for i in range(N + 1, 100001):
#     if i % 2 == 0:
#         DP[i] = min(DP[i-1] + 1, DP[i//2])
#     else:
#         DP[i] = DP[i-1] + 1

# print(DP[K])


################################
# 정석풀이 -> 0-1 BFS

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

#         if(0<=now +1 < 100000 and (now+1 not in visited or visited[now+1] > t+1)): 
#             queue.append((now+1,t+1))
#             visited[now+1] = t + 1
        
#         if(0<= now -1 < 100000 and (now-1 not in visited or visited[now-1] > t+1)):

#             queue.append((now-1,t+1))
#             visited[now-1] = t + 1

#         if(0<=now * 2 < 100000 and (now*2 not in visited or visited[now*2]>t)):
#             queue.appendleft((now*2,t))
#             visited[now*2] = t
#     return
        
        
# N, K = map(int,input().split())

# ans= 0

# bfs()

# print(ans)