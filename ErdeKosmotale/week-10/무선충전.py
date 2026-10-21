# row, col 뒤집혀 있음

# 순간 좌표에서 접속할 수 있는 모든 비콘

# 겹쳤을 때만 조합으로 처리하면 될 것 같음 a가 

T = int(input())

for test_case in range(1, T + 1):

    M , N_BC = map(int,input().split())

    A_route = list(map(int,input().split()))
    B_route = list(map(int,input().split()))

    lst= [[set() for _ in range(10)] for _ in range(10)]
    BC = []


    for i in range(N_BC):

        col, row, C, P = map(int,input().split())

        col-=1
        row-=1
        
        BC.append(P)

        for r in range(row-C,row+C+1,1):

            for c in range(col-C , col+C+1, 1):

                if(0<= r <10 and 0<=c< 10):

                    distance = abs((row)-r) +abs((col)-c)

                    if(distance<=C):
                        
                        lst[r][c].add(i)


    if(not lst[0][0]):
        A_grid = [-1] # 특정 시간에 범위에 들어오는 비콘들
    else:
        A_grid= [list(lst[0][0])]
    
    if(not lst[9][9]):
        B_grid = [-1]
    else:
        B_grid = [list(lst[9][9])]

    row_A = 0
    col_A = 0

    for cmd in A_route:

        if(cmd == 1):
            row_A -= 1

        elif(cmd== 2):
            col_A += 1

        elif(cmd == 3):
            row_A += 1

        elif(cmd == 4):
            col_A -= 1

        if(not lst[row_A][col_A] ):
            A_grid.append(-1)

        else:
            A_grid.append(list(lst[row_A][col_A]))        

    row_B = 9
    col_B = 9

    for cmd in B_route:
    
        if(cmd == 1):
            row_B -= 1

        elif(cmd== 2):
            col_B += 1

        elif(cmd == 3):
            row_B += 1

        elif(cmd == 4):
            col_B -= 1

        if(not lst[row_B][col_B] ):
            B_grid.append(-1)

        else:
            B_grid.append(list(lst[row_B][col_B])) 

    score = 0

    
    for i in range(M):

        A = A_grid[i]
        B = B_grid[i]

        A_max = 0
        B_max = 0
        score_sum = 0

        if(A==-1 and B== -1):
            continue

        elif(A==-1 and B != -1):

            for j in range(len(B)):
                B_max = max(B_max,BC[B[j]])

        elif(A!=-1 and B == -1):

            for j in range(len(A)):
                A_max = max(A_max,BC[A[j]])

        else:

            for j in range(len(A)):
                for k in range(len(B)):

                    if(BC[A[j]] == BC[B[k]]):
                        score_sum = max(score_sum,BC[A[j]])

                    else:
                        score_sum = max(score_sum, BC[A[j]]+BC[B[k]])    
                    
        score += A_max + B_max + score_sum


    print(f"#{test_case} {score}")


            