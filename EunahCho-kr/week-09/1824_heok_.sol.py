# 1824. 혁진이의 프로그램 검증
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4yLUiKDUoDFAUx&categoryId=AV4yLUiKDUoDFAUx&categoryType=CODE&problemTitle=1824&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 10:00 ~~

"""
<	이동 방향을 왼쪽으로 바꾼다. dr, dc = 0, -1
>	이동 방향을 오른쪽으로 바꾼다. dr, dc = 0, 1
^	이동 방향을 위쪽으로 바꾼다. dr, dc = 1, 0
v	이동 방향을 아래쪽으로 바꾼다. dr, dc = -1, 0
_	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
|	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.?? DIRECTIONS[random]
.	아무 것도 하지 않는다. dr, dc = 0, 1
@	프로그램의 실행을 정지한다. RETURN!!
0~9	메모리에 문자가 나타내는 값을 저장한다. dr, dc = 0, 1
+	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다. dr, dc = 0, 1
-	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다. dr, dc = 0, 1
"""

import sys
import random
sys.stdin = open('1824_input.txt', 'r')

DIRECTIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)] ## 좌우상하

def search(cmd, mmr):
    global R, C
    r = c = 0
    dr, dc = DIRECTIONS[1] # 초기값 -> 오른쪽
    visited = []
    visited.append((r, c))

    while True:
        # print(r, c)
        # <	이동 방향을 왼쪽으로 바꾼다. dr, dc = 0, -1
        if cmd[r][c] == "<":
            dr, dc = DIRECTIONS[0]

        # >	이동 방향을 오른쪽으로 바꾼다. dr, dc = 0, 1
        if cmd[r][c] == ">":
            dr, dc = DIRECTIONS[1]

        # ^	이동 방향을 위쪽으로 바꾼다. dr, dc = 1, 0
        if cmd[r][c] == "^":
            dr, dc = DIRECTIONS[2]

        # v	이동 방향을 아래쪽으로 바꾼다. dr, dc = -1, 0
        if cmd[r][c] == "v":
            dr, dc = DIRECTIONS[3]

        # _	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
        if cmd[r][c] == "_":
            if mmr[r][c] == 0:
              dr, dc = DIRECTIONS[1]
            else:
              dr, dc = DIRECTIONS[0]

        # |	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
        if cmd[r][c] == "|":
            if mmr[r][c] == 0:
              dr, dc = DIRECTIONS[3]
            else:
              dr, dc = DIRECTIONS[2]

        # ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.?? DIRECTIONS[random]
        if cmd[r][c] == "?":
            dr, dc = DIRECTIONS[random.randrange(3)]
            # print(dr, dc)

        # @	프로그램의 실행을 정지한다. RETURN!!
        if cmd[r][c] == "@":
            return 'YES'

        # 0~9	메모리에 문자가 나타내는 값을 저장한다.
        # if cmd[r][c] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if cmd[r][c] in map(str, range(10)):
            mmr[r][c] = int(cmd[r][c])

        # +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
        if cmd[r][c] == "+":
            if mmr[r][c] == 15:
                mmr[r][c] = 0
            else:
                mmr[r][c] += 1

        # -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다. dr, dc = 0, 1
        if cmd[r][c] == "-":
            if mmr[r][c] == 0:
                mmr[r][c] = 15
            else:
                mmr[r][c] -= 1


        # .	아무 것도 하지 않는다. dr, dc = 0, 1
            
        if (r + dr, c + dc) in visited:
            return 'NO'
        
        r += dr
        c += dc
        visited.append((r, c))

        if r == -1:
            r = R - 1
        elif r == R:
            r = 0

        if c == -1:
            c = C - 1
        elif c == C:
            c = 0


        
T = int(input())
for tc in range(1, T + 1):
    # if tc == 3:
    R, C = map(int, input().split())

    cmd = []
    for _ in range(R):
        tmp = []
        for c in input():
            tmp.append(c)
        cmd.append(tmp)

    mmr = [[0] * C for _ in range(R)]
    ans = search(cmd, mmr)
    print(f"#{tc} {ans}")