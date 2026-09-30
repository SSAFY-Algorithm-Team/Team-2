# 1949 SWEA 등산로  조성
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&
# 시간 2h / 시도

"""
등산로는 가장 높은 곳에서 시작
높은 -> 낮은 / 가로 / 세로 로만 연결 가능
딱 한 곳을 정해서 최대 k 깊이만큼 지형을 깎는 공사를 할 수 있음
15 sec

가장 긴 등산로 찾기
"""

import sys
sys.stdin = open('1949_input.txt', 'r')


DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find_max(field):
    max_val = max([max(row) for row in field])
    for r in range(n):
        for c in range(n):
            if field[r][c] == max_val:
                yield r, c


def search(n, k, start, field):
    x, y = start # 시작 좌표 (가장 높은 곳)
    is_used = False  # 산 깎았는지
    res = 0 # 최종 정답

    def dfs(x, y, h, d):
        nonlocal res, is_used

        res = max(res, d) # 매번 최대값으로 갱신

        if d == n * n + 1:  # 끝까지 돌았으면 return ==> 혹시 몰라서 넣었는데 visited땜에 필요 없을 듯
            return
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # 공통 조건 : 격자 안에 있고, 방문 안했어야함
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 우선 조건 : 새로운 곳이 현재보다 낮아야함
                if h > field[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, field[nx][ny], d + 1)
                    visited[nx][ny] = False
                # 우선 조건에서 못 들어갔다면, k번 깎을 수 있는 기회 1번
                elif not is_used: # 아직 기회 안썼으면
                    # 1 ~ k번 한번씩 깎아봄
                    for i in range(1, k + 1):
                        new_h = field[nx][ny] - i
                        is_used = True
                        # 깎은 높이가 현재보다 낮다면
                        if h > new_h:
                            visited[nx][ny] = True
                            dfs(nx, ny, new_h, d + 1)
                            visited[nx][ny] = False
                        # 다 탐색했으면(깎아봤으면) 다시 기회 부여 => 봉우리를 깎은 좌표인 nx, ny에서 빠져나왔으므로
                        is_used = False

    visited[x][y] = True 
    dfs(x, y, field[x][y], 1)
    visited[x][y] = False

    return res


T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    best = 0
    for start in find_max(field):
        res = search(n, k, start, field)
        best = max(best, res)
    print(f"#{tc} {best}")

"""
BFS 시도했는데 실패함!!

from collections import deque

def search(n, k, start, field):
    x, y = start
    # print(start)
    queue = deque([(x, y, field[x][y], 1)]) # 시작좌표, 지금 산의 높이, 지금까지 온 거리
    is_used = False  # 산 깎았는지
    # dist = [[0] * n for _ in range(n)]
    # dist[x][y] = 1

    res = 0
    while queue:
        x, y, h, d = queue.pop()
        res = max(res, d) # 최대값 갱신

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # 새로 가는 곳이 범위 안에 있고, 아직 안가봤으면
            if 0 <= nx < n and 0 <= ny < n: # and not dist[nx][ny]:
              # 지금 있는 곳보다 낮은 곳이면 갈 수 있음
              if field[nx][ny] < h:
                  queue.append((nx, ny, field[nx][ny], d + 1))
                  # dist[nx][ny] = dist[x][y] + 1
              # 근데 만약 산을 깎을 기회가 남아있다면? -> k만큼 깎아버리자!
              elif not is_used:
                  new_h = field[nx][ny] - k
                  if new_h < h:
                      is_used = True
                      queue.append((nx, ny, new_h, d + 1))
                      # dist[nx][ny] = dist[x][y] + 1

    # for row in dist:
    #     print(row)
    
    # res = max(max(row) for row in dist)
    return res
"""