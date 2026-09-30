def Queen(N):
    result = 0
    # 인덱스가 각 행이고, 저장되는 좌표값이 열
    board = [-1] * N
    def dfs(row):
        nonlocal result
        # N개를 다 저장했다면 row == N 결과 +1
        if row ==N:
            result +=1
            return
        # 새로운 행의 열을 0부터 탐색
        for col in range(N):
            possible = True
            # board에 저장된 이전 행들의 세로,대각선 값 확인/ 가로값의 경우는 row로 관리하고 있어서 확인할 필요 없음
            for prev_row in range(row):
                if board[prev_row] == col or abs(prev_row - row) == abs(board[prev_row] - col):
                    possible = False
                    break
            # 겹치지 않는 곳에 퀸을 배치했다면 다음 행 탐색
            if possible:
                board[row] = col
                dfs(row+1)
    dfs(0)
    return result
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans = Queen(N)
    print(f"#{tc} {ans}")




