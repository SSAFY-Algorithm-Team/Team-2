def find_start():

    start_row, start_col = 0,0

    end_row , end_col = 0,0

    for r in range(16):
        for c in range(16):
            if(lst[r][c]==2):
                start_row,start_col = r, c

            if(lst[r][c]==3):
                end_row, end_col = r,c

    return start_row,start_col,end_row,end_col

from collections import deque

DIRECTION = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우

def bfs():

    queue = deque()
    queue.append((start_row,start_col))

    while(queue):

        c_row,c_col = queue.popleft()

        for r,c in DIRECTION:

            n_row = c_row + r
            n_col = c_col + c

            if(0<=n_row<16 and 0<=n_col<16):
                if(lst[n_row][n_col]==3):
                    return 1

                elif(lst[n_row][n_col]==0):
                    queue.append((n_row,n_col))

            lst[c_row][c_col]=1

    return 0


for test_case in range(1,11):

    garbage= int(input())

    lst = [list(map(int,input())) for _ in range(16)]

    start_row,start_col,end_row,end_col = find_start()

    ans = bfs()

    print(f"#{test_case} {ans}")