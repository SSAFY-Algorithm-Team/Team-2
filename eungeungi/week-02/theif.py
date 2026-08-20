# 출발점을 입력으로 둠
# 각 터널 구조물 타입에 따른 dx,dy를정함
# 1타입은 4방향, 2타입은 상,하 등 아래와 같이
# dir = [[(-1,0),(1,0),(0,1),(0,-1)],[(0,1),(0,-1)]] 
# 재귀함수를 계속 호출하여 소요시간만큼 반복
# 함수 내에선 지속해서 다음값으로 이동, false였던 값들 방문하는 순간 true
# 기존 행렬값들 false로 해둔 뒤, 시작점포함 true로 변경된값들 합 return


from collections import deque

# 방향 인덱스: 0=상, 1=하, 2=좌, 3=우
OPPOSITE = {0: 1, 1: 0, 2: 3, 3: 2}

# 각 방향 인덱스에 대응하는 (dx, dy) 이동량
DXY = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

# 터널 타입별 방향들 (그대로 매핑)
TYPE_DIR = {
    1: [0, 1, 2, 3],  # 십자: 상하좌우
    2: [0, 1],        # 세로: 상하
    3: [2, 3],        # 가로: 좌우
    4: [0, 3],        # ㄴ자 형태: 상,우
    5: [1, 3],        # 상,우 반대꺾임: 하,우
    6: [1, 2],        # 하,좌
    7: [0, 2],        # 상,좌
}


def cal(N, M, R, C, L, arr):
    # dist[i][j] = 출발점에서 (i,j)까지 최단 도달 시간, -1이면 아직 미방문
    dist = [[-1] * M for _ in range(N)]
    dist[R][C] = 0  # 출발점은 0시간에 위치

    queue = deque()
    queue.append((R, C))

    while queue:
        x, y = queue.popleft()
        cur_type = arr[x][y]
        if cur_type == 0:  # 터널이 없는 칸이면 스킵 (이론상 안 오지만 안전장치)
            continue

        # 현재 칸이 열려있는 방향들만 순회
        for d in TYPE_DIR.get(cur_type, []):
            dx, dy = DXY[d]
            nx, ny = x + dx, y + dy

            # 지도 범위를 벗어나면 무시
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            next_type = arr[nx][ny]
            if next_type == 0:  # 이웃 칸에 터널이 없으면 이동 불가
                continue

            # 양방향 연결 체크: 이웃 칸이 "반대 방향"으로 열려 있어야 실제로 연결된 것
            opp = OPPOSITE[d]
            if opp not in TYPE_DIR.get(next_type, []):
                continue

            # 처음 방문하는 칸이면 최단시간 기록하고 큐에 추가 (BFS라 이때가 최단거리 확정)
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    # 방문된 칸(dist != -1) 중, L시간 이내로 도달 가능한 칸의 개수를 카운트
    count = 0
    for i in range(N):
        for j in range(M):
            if dist[i][j] != -1 and dist[i][j] <= L:
                count += 1
    return count


T = int(input())  
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  
    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)  

    ans = cal(N, M, R, C, L, arr)  
    print(f"#{tc} {ans}")  