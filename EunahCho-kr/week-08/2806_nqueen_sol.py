# 2806 SWEA N-Queens 
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB&
# 시간 1h, 시도 1


import sys


QUEENS = []


def check(r, c):
    # print("check", r, c)
    for q_r, q_c in QUEENS:
      # 같은 행 검사
      if q_r == r:
          return False  
      # 같은 열 검사
      if q_c == c:
          return False
      # 오른쪽 대각선 검사 -> r + c합이 같은 말 있으면 안됨
      if q_r + q_c == r + c:
          return False

    # 왼쪽 대각선 검사 -> r - i, c - i에 해당하는 말 있으면 안됨
    while r >= 0 and c >= 0:
        if (r, c) in QUEENS:
            return False
        r -= 1
        c -= 1

    return True


def solve(n):
    cnt = 0

    def dfs(r):
        nonlocal cnt
        # print(QUEENS)

        if len(QUEENS) == n:
            cnt += 1
            return

        # 다음 행에서 무슨열 고를지
        for qc in range(n):
            qr = r + 1
            if 0 <= qr < n and 0 <= qc < n:
              if check(qr, qc):
                  QUEENS.append((qr, qc))
                  dfs(qr)
                  QUEENS.pop()

    # 시작열 지정
    for c in range(n):
      QUEENS.append((0, c))
      dfs(0)
      QUEENS.pop()

    return cnt


def main():
    sys.stdin = open('2806_input.txt', 'r')
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        ans = solve(n)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    main()