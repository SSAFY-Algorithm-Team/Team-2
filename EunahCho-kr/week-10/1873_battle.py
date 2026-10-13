# SWEA 1873 상호의 배틀필드
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LyE7KD2ADFAXc&categoryId=AV5LyE7KD2ADFAXc&categoryType=CODE&problemTitle=1873&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 1h 30m  / 시도 2

# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)

# 모든 입력을 처리하고 나면 게임 맵의 상태가 어떻게 되는지

import sys
sys.stdin = open('1873_input.txt', 'r')

DIRECRIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # U D L R

PAIRS = {
    "U": ["^", 0], "^": 0,
    "D": ["v", 1], "v": 1,
    "L": ["<", 2], "<": 2,
    "R": [">", 3], ">": 3,
}

def solve(cmds, board, h, w):

    for r in range(h):
        for c in range(w):
            if board[r][c] in "><^v":
                cr, cc = r, c

    for cmd in cmds:
      if cmd == 'S':
      # S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
          dr, dc = DIRECRIONS[PAIRS[board[cr][cc]]]
          tr, tc = cr + dr, cc + dc
          while 0 <= tr < h and 0 <= tc < w:
          # 포탄은 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진한다.
          # 포탄이 벽에 부딪히면 포탄은 소멸하고, 부딪힌 벽이 벽돌로 만들어진 벽이라면 이 벽은 파괴되어 칸은 평지가 된다.
              if board[tr][tc] == "*":
                  board[tr] = board[tr][:tc] + "." + board[tr][tc + 1:]
                  break

              if board[tr][tc] == "#":
                  break

              tr += dr
              tc += dc
          
      else:
      # U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
      # D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
      # L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
      # R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
          new_d = PAIRS[cmd][0]
          board[cr] = board[cr][:cc] + new_d + board[cr][cc + 1:] 
          ## 디버깅한 부분 => 이 부분이 아래 if문 안에 있었는데, 새로운 칸으로 갈 수 있던, 없던 방향은 바꿔야하므로 맨 처음으로 바꿨다.
          
          dr, dc = DIRECRIONS[PAIRS[cmd][1]]
          nr, nc = cr + dr, cc + dc
          if 0 <= nr < H and 0 <= nc < W:
              if board[nr][nc] == '.':
                  board[cr] = board[cr][:cc] + "." + board[cr][cc + 1:]
                  board[nr] = board[nr][:nc] + new_d + board[nr][nc + 1:]
                  cr, cc = nr, nc

      # for row in board:
      #     print(row)
      # print(cmd, ' 끝')

    return


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = [input() for _ in range(H)]
    _ = int(input())
    cmds = input()
    solve(cmds, board, H, W)

    print(f"#{tc}", end = " ")
    for row in board:
        print(row)
  