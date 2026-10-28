# 0은 홈부분 1은 돌기 부분
def rotate(key):
    m = len(key)
    new = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new[i][j] = key[m - 1 - j][i]
    return new

def check(board, m, n):
    # 가운데 N×N(자물쇠 영역)이 전부 1인지 확인
    for i in range(m - 1, m - 1 + n):
        for j in range(m - 1, m - 1 + n):
            if board[i][j] != 1:
                return False
    return True

def solution(key, lock):
    
    n, m = len(lock), len(key)
    size = n + 2 * (m - 1)

    # 1. 0으로 채운 큰 판 만들기
    board = [[0] * size for _ in range(size)]

    # 2. 가운데에 자물쇠 복사 (M-1만큼 밀어서)
    for i in range(n):
        for j in range(n):
            board[i + m - 1][j + m - 1] = lock[i][j]
    
        # 3. 회전 4번 × 모든 위치 시도
    for _ in range(4):
        for row in range(n + m - 1):
            for col in range(n + m - 1):
                # 열쇠 더하기
                for i in range(m):
                    for j in range(m):
                        board[row + i][col + j] += key[i][j]

                # 자물쇠 영역이 전부 1이면 열림
                if check(board, m, n):
                    return True

                # 열쇠 빼기 (원상복구)
                for i in range(m):
                    for j in range(m):
                        board[row + i][col + j] -= key[i][j]

        key = rotate(key)
    
    return False


