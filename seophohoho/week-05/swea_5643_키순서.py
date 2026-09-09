# import sys
# input = sys.stdin.readline
from collections import deque

def calc(gra, start, n):
    visited = [False] * (n+1)
    visited[start] = True
    que = deque([start])
    cnt = 0

    while que:
        node = que.popleft()
        for naver in gra[node]:
            if not visited[naver]:
                visited[naver] = True
                cnt += 1
                que.append(naver)

    return cnt

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    M = int(input())

    gra = [[] for _ in range(N+1)] #정방향 그래프
    r_gra = [[] for _ in range(N+1)] #역방향 그래프

    for _ in range(M):
        a,b = map(int,input().split())
        gra[a].append(b)
        r_gra[b].append(a)


    answer = 0
    for targets in range(1,N+1):
        small = calc(r_gra,targets,N)
        big = calc(gra,targets,N)

        if small + big == N-1:
            answer += 1

    print(f'#{tc} {answer}')