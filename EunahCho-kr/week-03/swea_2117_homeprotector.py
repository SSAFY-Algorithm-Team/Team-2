# SWEA 2117 홈 방범 서비스
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu
# 시간 4h 30m / 시도 3

from collections import deque


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def calculate(k, home_cnt, m):
    profit = (home_cnt * m) - (k * k + (k - 1) * (k - 1))
    if profit >= 0:
        return True
    else:
        return False


def bfs(n, k, homes, starts):

    start_r, start_c = starts

    queue = deque([(start_r, start_c)])
    visited = [[False] * n for _ in range(n)]
    visited[start_r][start_c] = True
    cnt = 0
    if homes[start_r][start_c]: # 첫 위치에 집이 있다면, 그거도 세야함
        cnt += 1

    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if abs(nr - start_r) + abs(nc - start_c) < k:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    if homes[nr][nc]:
                        cnt += 1
    return cnt


def solve(n, m, homes):
    if n % 2 == 0:
        k = n + 1
    else:
        k = n

    max_cnt = 0

    while k > 0: 
        for x in range(n):
            for y in range(n):
                home_cnt = bfs(n, k, homes, (x, y))
                if calculate(k, home_cnt, m):
                    max_cnt = max(max_cnt, home_cnt)
        k -= 1

    return max_cnt  


def main():
    T = int(input())
    for t in range(1, T+1):
        n, m = map(int, input().split())
        homes = [list(map(int, input().split())) for _ in range(n)]
        ans = solve(n, m, homes)
        print(f"#{t} {ans}")
        

if __name__ == "__main__":
    main()


# 두번째 접근 : 첫번째 집에서 가장 먼 집까지 거리 - k : 이익 따져보기 => k하나씩 줄이기 ==> 두번째 집에서 ~ 

"""
집 위치 다 따기
- 한 집에서 시작 -> k = 1거리에 있는 집 수 셈 (bfs) -> k = 2거리에,, -> k가 다 덮어버리면 

"""

"""
첫시도 였던것
# 첫 접근 : 왼쪽 맨 위에 맵 만드는 함수 -> direction 따라 움직일 수 있는 함수 만듦 -> bfs로 지정된 영역 내 집 개수 세는 함수 만듦 -> 가장 큰 맵에서 시작해서 크기를 하나씩 줄이기 + 위치 조정으로 손해가 아닌 최대 집 수 구함

from collections import deque
from pprint import pprint


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def make_map(k, n):
    area = [[0] * n for _ in range(n)]

    start, end = 0, 2 * k - 1
    hu = hd = k - 1

    while start <= end:
        for i in range(start, end):
            area[hu][i] = 1
            area[hd][i] = 1
        start += 1
        end -= 1
        hu += 1
        hd -= 1
    return area

# mapp = make_map(3, 10)
# pprint(mapp)

def move_map(area, direction):
    dr, dc = direction
    n = len(area)
    new_area = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if 0 <= row + dr < n and 0 <= col + dc < n:
                new_area[row + dr][col + dc] = area[row][col]
    return new_area

# area = make_map(3, 10)
# pprint(move_map(area, (1, 0)))

def calculate(k, home_cnt, m):
    profit = (k * k + (k - 1) * (k - 1)) - (home_cnt * m)
    if profit >= 0:
        return True
    else:
        return False


def bfs(n, homes, area):
    for row in range(n):
        for col in range(n):
            if homes[row][col] and area[row][col]:
                start_r = row
                start_c = col
                break

    queue = deque([start_r, start_c])
    visited = [[False] * n for _ in range(n)]
    visited[start_r][start_c] = True
    cnt = 0

    while queue:
        r, c = queue.popleft
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if  area[nr][nc] and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                    if homes[nr][nc]:
                        cnt += 1
    return cnt


def solve(n, m, homes):
    if n % 2 == 0:
        k = n + 1
    else:
        k = n

    max_cnt = 0

    while k > 0: 
        area = make_map(k, n)
        home_cnt = bfs(n, homes, area)
        if calculate(k, home_cnt, m):
            max_cnt = max(max_cnt, home_cnt) # 첫 위치에서 시도
            # 가지치기 하고 싶다!!!!!!!!!!!!!

        for direction in DIRECTIONS: # 이동하면서 세보기 => 여기서도 bfs를 써야할 것만 같은 느낌
            while area: # area에 값이 남아 있을 때까지
                area = move_map(area, direction)
                home_cnt = bfs(n, homes, area)
                if calculate(k, home_cnt, m):
                    max_cnt = max(max_cnt, home_cnt)

        k -= 1

    return max_cnt  


def main():
    T = int(input())
    for t in range(1, T+1):
        n, m = map(int, input().split())
        homes = [list(map(int, input().split())) for _ in range(n)]
        ans = solve(n, m, homes)
        print(f"#{t} {ans}")
        

if __name__ == "__main__":
    main()
"""