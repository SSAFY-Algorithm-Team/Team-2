# 4014. [모의 SW 역량테스트] 활주로 건설
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH&categoryId=AWIeW7FakkUDFAVH&categoryType=CODE&problemTitle=4014&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 936~

import sys
sys.stdin = open('4014_input.txt', 'r')



def solve(board, n, x):
    ans = 0

    # 가로 기준
    for r in range(n):
        seq = 1
        streak = 0
        s_seq = 0
        is_completed = True

        for c in range(n - 1):
            
            if streak:
                streak -= 1
                s_seq += 1
                continue

            if board[r][c] == board[r][c + 1]:
                # print("c -", c)
                seq += 1

            else:
                if board[r][c] - board[r][c + 1] == -1: # 경사를 올라갈 때
                    # print("c up", c)
                    if seq < x or s_seq not in [0, x]:
                        is_completed = False
                        # print(seq, s_seq, 'up')
                        break

                elif board[r][c] - board[r][c + 1] == 1: # 경사를 내려갈 때
                    # print("c down", c)

                    for t in range(1, x + 1):
                        if c + t >= n: # 범위 벗어나면 설치 못함
                            is_completed = False
                            # print('down, oor')
                            break

                        if board[r][c + 1] != board[r][c + t]: # 활주로 놓을 곳에 높이 달라지면 설치 못함
                            is_completed = False
                            # print('down, heights')
                            break

                        streak = x - 1 # 앞으로 x길이 만큼은 탐색 뛰어넘을거임 (맨 위 if)

                    if not streak:
                        break

                seq = 1 # 한 번 달라졌으면 seq은 초기화

        if is_completed and not streak:
            # print(r)
            ans += 1

    # print("ans!!!!!!!!!!!!", ans)

    # 세로 기준
    for c in range(n):
        seq = 1
        streak = 0
        s_seq = 0
        is_completed = True

        for r in range(n - 1):
            
            if streak:
                streak -= 1
                s_seq += 1
                continue

            if board[r][c] == board[r + 1][c]:
                # print("c -", c)
                seq += 1

            else:
                if board[r][c] - board[r + 1][c] == -1: # 경사를 올라갈 때
                    # print("c up", c)
                    if seq < x or s_seq not in [0, x]:
                        is_completed = False
                        # print(seq, s_seq, 'up')
                        break

                elif board[r + 1][c] - board[r][c] == 1: # 경사를 내려갈 때
                    # print("c down", c)

                    for t in range(1, x + 1):
                        if r + t >= n: # 범위 벗어나면 설치 못함
                            is_completed = False
                            # print('down, oor')
                            break

                        if board[r + 1][c] != board[r + t][c]: # 활주로 놓을 곳에 높이 달라지면 설치 못함
                            is_completed = False
                            # print('down, heights')
                            break

                        streak = x - 1 # 앞으로 x길이 만큼은 탐색 뛰어넘을거임 (맨 위 if)

                    if not streak:
                        break

                seq = 1 # 한 번 달라졌으면 seq은 초기화

        if is_completed and not streak:
            # print(r)
            ans += 1

    return ans


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = solve(board, N, X)
    print(f"#{tc} {ans}")



"""
## claude 새로짬

기존 코드의 문제점

오르막 조건이 틀림: s_seq != x를 검사하는데, 올라갈 때 필요한 조건은 "앞쪽에 같은 높이의 비어 있는 칸이 x개 이상"이에요. s_seq는 이 조건과 관계가 없어요.
내리막 경사로 칸이 재사용됨: 내리막에 쓴 칸을 streak으로 건너뛰지만, 그 뒤 seq = 1로 초기화하기 때문에 이미 경사로가 놓인 칸이 오르막 경사로 길이에 다시 포함돼요. 그래서 [Fig. 10]처럼 겹치는 경우를 잡지 못해요.
높이 차이가 2 이상인 경우를 처리하지 않음: 이때는 바로 실패여야 하는데 그냥 넘어가요.
실패 처리가 꼬임: 안쪽 for t 루프에서 break해도 streak이 이미 설정돼 있을 수 있어서, 바깥 루프가 계속 돌아요.
solve가 값을 return하지 않고, 세로 방향 처리가 비어 있어요.

핵심 아이디어: cnt 하나로 관리하기

cnt는 현재 높이에서 연속으로 비어 있는 칸 수예요.
같은 높이면 cnt += 1 해요.
오르막이면 cnt >= x여야 설치할 수 있어요. 설치한 뒤 cnt = 1로 둬요.
내리막이면 cnt >= 0이어야 해요(이전 내리막 경사로가 다 깔렸는지 확인). 그 뒤 cnt = 1 - x로 둬요. 앞으로 x칸이 필요하다는 뜻으로 음수를 빚처럼 쓰는 거예요.
끝까지 간 뒤 cnt >= 0이면 성공이에요. 내리막 경사로가 지도 밖으로 나가는 경우도 여기서 걸러져요.

import sys
sys.stdin = open('4014_input.txt', 'r')


def can_build(line, n, x):
    cnt = 1  # 현재 높이에서 연속으로 비어 있는 칸 수
    for i in range(1, n):
        diff = line[i] - line[i - 1]

        if diff == 0:
            cnt += 1
        elif diff == 1:            # 오르막: 뒤쪽 낮은 칸 x개 필요
            if cnt < x:
                return False
            cnt = 1
        elif diff == -1:           # 내리막: 앞쪽 낮은 칸 x개 필요
            if cnt < 0:            # 이전 내리막 경사로가 아직 덜 깔림
                return False
            cnt = 1 - x
        else:                      # 높이 차 2 이상
            return False

    return cnt >= 0                # 마지막 내리막 경사로가 다 깔렸는지


def solve(board, n, x):
    ans = 0
    for row in board:              # 가로
        if can_build(row, n, x):
            ans += 1
    for col in zip(*board):        # 세로
        if can_build(col, n, x):
            ans += 1
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {solve(board, N, X)}')
"""


"""
내 코드에서 고친거 (클로드)
import sys
sys.stdin = open('4014_input.txt', 'r')


def solve(board, n, x):
    ans = 0

    # 가로 기준
    for r in range(n):
        seq = 1
        streak = 0
        s_seq = 0
        is_completed = True

        for c in range(n - 1):

            if streak:
                streak -= 1
                s_seq += 1
                continue

            if board[r][c] == board[r][c + 1]:
                seq += 1

            else:
                if board[r][c] - board[r][c + 1] == -1:  # 경사를 올라갈 때
                    if seq < x:  # ✅ s_seq 조건 삭제
                        is_completed = False
                        break
                    seq = 1  # ✅ 오르막 뒤에는 새 높이에서 1칸부터 시작

                elif board[r][c] - board[r][c + 1] == 1:  # 경사를 내려갈 때
                    for t in range(1, x + 1):
                        if c + t >= n:
                            is_completed = False
                            break
                        if board[r][c + 1] != board[r][c + t]:
                            is_completed = False
                            break
                        streak = x - 1

                    if not is_completed:  # ✅ 실패하면 바로 종료
                        break
                    seq = 0  # ✅ 내리막 경사로가 깔린 칸은 비어 있지 않음

                else:  # ✅ 높이 차 2 이상이면 실패
                    is_completed = False
                    break

        if is_completed and not streak:
            ans += 1

    # 세로 기준
    for c in range(n):
        seq = 1
        streak = 0
        s_seq = 0
        is_completed = True

        for r in range(n - 1):

            if streak:
                streak -= 1
                s_seq += 1
                continue

            if board[r][c] == board[r + 1][c]:
                seq += 1

            else:
                if board[r][c] - board[r + 1][c] == -1:  # 경사를 올라갈 때
                    if seq < x:  # ✅
                        is_completed = False
                        break
                    seq = 1  # ✅

                elif board[r][c] - board[r + 1][c] == 1:  # ✅ 부호 수정 (내리막)
                    for t in range(1, x + 1):
                        if r + t >= n:
                            is_completed = False
                            break
                        if board[r + 1][c] != board[r + t][c]:
                            is_completed = False
                            break
                        streak = x - 1

                    if not is_completed:  # ✅
                        break
                    seq = 0  # ✅

                else:  # ✅
                    is_completed = False
                    break

        if is_completed and not streak:
            ans += 1

    return ans


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = solve(board, N, X)
    print(f"#{tc} {ans}")
"""