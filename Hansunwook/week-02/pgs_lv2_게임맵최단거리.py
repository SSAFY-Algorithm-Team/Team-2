#큐 import
from collections import deque

def solution(maps):
    answer = 0
    #초기 접근
    # 일단 아래위양옆 배열 만들고
    # 만약 그냥 상대방 진영에 벽 다 있으면 그냥 result -1 해서 끝
    # bfs로 너비우선 탐색
    # deque로 ?
    
    ud = [1,-1,0,0]
    rl = [0,0,1,-1]
    
    #큐 만들기
    queue = deque()
    
    N = len(maps)
    M = len(maps[0])

    #
    #visit = [[False] * m for _ in range(n)]
    #방문 여부 확인
    visit = []
    for i in range(N):
        visit.append([False]*M)
        
    # 거리 기록
    distance = []
    for i in range(N):
        distance.append([0] * M)
        
    visit[0][0] = True
    distance[0][0] = 1
    queue.append((0, 0))
    
    while queue:
        a,b = queue.popleft()
        
        for i in range(4):
            an = a + ud[i]
            bn = b + rl[i]
            
            # 맵 밖이면
            if an < 0 or an >= N or bn < 0 or bn >= M:
                continue
            
            # 벽이면
            if maps[an][bn] == 0:
                continue
            
            # 이미 방문했으면
            if visit[an][bn]:
                continue
            
            distance[an][bn] = distance[a][b] + 1
            visit[an][bn] = True
            queue.append((an,bn))
    
    if visit[N-1][M-1]:
        answer = distance[N-1][M-1]
        return answer

    answer = -1
    return answer