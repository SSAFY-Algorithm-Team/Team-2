def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    # 겹치지 않기위해 set 설정
    boom = set()
    # boom 될때까지 반복
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] !='0' and board[i][j] == board[i+1][j] and board[i][j]== board[i+1][j+1] and board[i][j] == board[i][j+1] : 
                    boom.add((i,j))
                    boom.add((i+1,j))
                    boom.add((i,j+1))
                    boom.add((i+1,j+1))
        # boom이 없는 경우 그대로 반복문 끝내
        if len(boom) == 0:
            break
        answer += len(boom)
        # boom된 좌표들 일단 0으로 채워
        for x,y in boom:
            board[x][y] = '0'
        # boom 초기화
        boom = set()
        # 자리 재배정
        for j in range(n):
            stack = []
            for i in range(m):
                # 열별로 체크하면서 0이 아닌 값들만 stack에 넣기
                if board[i][j] !='0':
                    stack.append(board[i][j])
            # stack에 값이 있다면 아래서부터 채우기
            for i in range(m-1,-1,-1):
                if stack:
                    board[i][j] = stack.pop()
                # 빈 값은 0으로 채움 - boom으로 없어진 값들(사이값도 포함)
                else:
                    board[i][j] ='0'
            # 이 과정이 끝나면 재배치가 됐으니 다시 while문 돌게됨
    
    return answer

