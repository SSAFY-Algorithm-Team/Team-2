from collections import deque
def bfs(N,M):
    queue = deque()
    queue.append((N,0))
    visited = [False] * 1000001
    visited[N] = True
    while queue:
        num, cnt = queue.popleft()
        if num == M:
            return cnt
        nxt_num = [num+1, num-1, num*2, num-10]
        for number in nxt_num:
            if 1<= number <=1000000 and not visited[number]:
                visited[number] = True
                queue.append((number,cnt+1))

        

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    ans = bfs(N,M)
    print(f"#{tc} {ans}")