# 5105. 미로의 거리
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTVoHTab5gDFAVT&categoryId=AWTVoHTab5gDFAVT&categoryType=CODE&problemTitle=5105&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 시간 20m 시도 1

"""
nn크기 미로 / 출발지2 / 목적지3
최소 몇 개 칸을 지나면 출발지에서 도착지 다다를 수 있는지?
"""
import sys
from collections import deque
sys.stdin = open('5105_input.txt', 'r')


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def search(n, board):
    for x in range(n):
        for y in range(n):
            if board[x][y] == 2:
                queue = deque([(x, y, 0)])

    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not board[nx][ny]:
                    queue.append((nx, ny, dist + 1))
                    board[nx][ny] = 1
                elif board[nx][ny] == 3:
                    return dist

    return 0 


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = []
    for _ in range(n):
        tmp = []
        for i in input():
            tmp.append(int(i))
        board.append(tmp)

    ans = search(n, board)
    print(f"#{tc} {ans}")