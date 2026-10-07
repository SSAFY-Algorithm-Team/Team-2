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

def search(cmd):
    global R, C
    r = c = 0
    d = 1 # 초기값 -> 오른쪽
    mmr = 0
    visited = set()
    visited.add((r, c, d, mmr))

    while True:
        print(r, c, d, mmr)
        print(cmd[r][c])


        # <	이동 방향을 왼쪽으로 바꾼다. dr, dc = 0, -1
        if cmd[r][c] == "<":
            d = 0

        # >	이동 방향을 오른쪽으로 바꾼다. dr, dc = 0, 1
        if cmd[r][c] == ">":
            d = 1

        # ^	이동 방향을 위쪽으로 바꾼다. dr, dc = 1, 0
        if cmd[r][c] == "^":
            d = 2

        # v	이동 방향을 아래쪽으로 바꾼다. dr, dc = -1, 0
        if cmd[r][c] == "v":
            d = 3

        # _	메모리에 0이 저장되어 있으면 이동 방향을 오른쪽으로 바꾸고, 아니면 왼쪽으로 바꾼다.
        if cmd[r][c] == "_":
            if mmr == 0:
                d = 1
            else:
                d = 0

        # |	메모리에 0이 저장되어 있으면 이동 방향을 아래쪽으로 바꾸고, 아니면 위쪽으로 바꾼다.
        if cmd[r][c] == "|":
            if mmr == 0:
                d = 3
            else:
                d = 2

        # ?	이동 방향을 상하좌우 중 하나로 무작위로 바꾼다. 방향이 바뀔 확률은 네 방향 동일하다.?? DIRECTIONS[random]
        if cmd[r][c] == "?":
            d = random.randrange(3)

        # @	프로그램의 실행을 정지한다. RETURN!!
        if cmd[r][c] == "@":
            return 'YES'

        # 0~9	메모리에 문자가 나타내는 값을 저장한다.
        # if cmd[r][c] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if cmd[r][c] in map(str, range(10)):
            mmr = int(cmd[r][c])

        # +	메모리에 저장된 값에 1을 더한다. 만약 더하기 전 값이 15이라면 0으로 바꾼다.
        if cmd[r][c] == "+":
            if mmr == 15:
                mmr = 0
            else:
                mmr += 1

        # -	메모리에 저장된 값에 1을 뺀다. 만약 빼기 전 값이 0이라면 15로 바꾼다. dr, dc = 0, 1
        if cmd[r][c] == "-":
            if mmr == 0:
                mmr = 15
            else:
                mmr -= 1


        # .	아무 것도 하지 않는다. dr, dc = 0, 1
        dr, dc = DIRECTIONS[d]
        nr, nc = r + dr, c + dc
        if (nr, nc, d, mmr) in visited:
            return 'NO'
        
        r += dr
        c += dc
        visited.add((nr, nc, d, mmr))

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
    R, C = map(int, input().split())

    cmd = []
    for _ in range(R):
        tmp = []
        for c in input():
            tmp.append(c)
        cmd.append(tmp)

    if tc == 13:
        print(cmd)
        ans = search(cmd)
        print(f"#{tc} {ans}")


"""
## 맞는 코드 (claude)

import sys
from collections import deque
sys.stdin = open('1824_input.txt', 'r')

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌 우 상 하


def search(cmd):
    # @가 없으면 절대 멈출 수 없음
    if not any('@' in row for row in cmd):
        return 'NO'

    start = (0, 0, 1, 0)  # r, c, d(오른쪽), mmr
    visited = {start}
    q = deque([start])

    while q:
        r, c, d, mmr = q.popleft()
        ch = cmd[r][c]
        next_dirs = None

        if ch == '@':
            return 'YES'
        elif ch == '<':
            d = 0
        elif ch == '>':
            d = 1
        elif ch == '^':
            d = 2
        elif ch == 'v':
            d = 3
        elif ch == '_':
            d = 1 if mmr == 0 else 0
        elif ch == '|':
            d = 3 if mmr == 0 else 2
        elif ch == '?':
            next_dirs = [0, 1, 2, 3]   # 네 방향 모두 탐색
        elif ch.isdigit():
            mmr = int(ch)
        elif ch == '+':
            mmr = 0 if mmr == 15 else mmr + 1
        elif ch == '-':
            mmr = 15 if mmr == 0 else mmr - 1
        # '.' 은 아무것도 안 함

        if next_dirs is None:
            next_dirs = [d]

        for nd in next_dirs:
            dr, dc = DIRECTIONS[nd]
            nr, nc = (r + dr) % R, (c + dc) % C   # wrap 먼저!
            state = (nr, nc, nd, mmr)
            if state not in visited:
                visited.add(state)
                q.append(state)

    return 'NO'   # 갈 수 있는 상태를 다 돌았는데 @ 못 만남


T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    cmd = [input()[:C] for _ in range(R)]
    print(f"#{tc} {search(cmd)}")
    
"""

"""
네 군데가 문제였어요. 그중 ? 처리와 방향 매핑 때문에 틀린 테스트케이스가 많이 나왔을 거예요.

1. 상/하 방향이 반대로 되어 있음
행 번호는 아래로 갈수록 커져요. 그래서 위쪽은 (-1, 0), 아래쪽은 (1, 0)이어야 해요. 지금 코드에서는 ^(d=2)가 (1, 0)이라 실제로는 아래로 움직여요.

2. ?를 랜덤으로 처리하면 안 됨 (핵심)
문제는 "정지할 수 있는가"를 묻고 있어요. 그래서 랜덤으로 한 방향만 골라 보는 게 아니라 4방향을 모두 탐색해야 해요. 그중 하나라도 @에 도달하면 YES예요. 게다가 random.randrange(3)은 0~2만 나와서 아래쪽(3)은 아예 뽑히지도 않아요.
→ 상태 (r, c, d, mmr)를 BFS로 탐색하는 방식으로 바꿨어요. 상태 수는 최대 20×20×4×16 = 25,600개라 충분히 빨라요.

3. visited 체크를 wrap 하기 전에 함
(nr, nc)가 -1이나 R일 수 있는 상태에서 visited를 확인하고 추가하고 있어요. 그래서 같은 상태를 다시 방문해도 감지되지 않아요. 좌표를 % R, % C로 먼저 감싼 다음 체크해야 해요.

4. 디버그 코드 정리
print(r, c, d, mmr), print(cmd[r][c]), if tc == 13: 같은 디버그용 코드가 남아 있으면 출력 형식이 틀려요.

추가로, 격자에 @가 아예 없으면 탐색할 필요 없이 바로 NO를 반환하도록 했어요.
"""