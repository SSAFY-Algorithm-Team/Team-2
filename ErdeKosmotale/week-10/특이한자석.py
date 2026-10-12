

# 2번의 좌표 << right
# 6번의 좌표 << left

# 특정 거 돌리면 그거보다 
# 1 작은거 오른쪽이랑 
# 1 큰 거 왼쪽 봐야해

# 일단 한 번 못풀었음

T = int(input())





for test_case in range(1,T + 1):

    K = int(input())

    lst_magnet = [list(map(int,input().split())) for _ in range(4)]

    left_lst  =  [ -1,6,6,6] # 왼쪽들
    right_lst =  [ 2,2,2,-1] # 오른쪽들
    red_lst   =  [0,0,0,0]   # 빨간색 부분

    for _ in range(K):

        magnet, direction = map(int,input().split())
        magnet -=1


        left_magnet = magnet - 1
        right_magnet = magnet + 1

        left_flag = 0    # 1이면 돌림, -1이면 반시계방향으로 돌림, 0이면 안돌림
        right_flag = 0   # 1이면 돌림, -1이면 반시계방향으로 돌림, 0이면 안돌림


        
        if(left_magnet != -1):

            if(lst_magnet[left_magnet][right_lst[left_magnet]] != lst_magnet[magnet][left_lst[magnet]]):

                left_flag = direction * (-1)
                

        if(right_magnet != 4):
            
            if(lst_magnet[right_magnet][left_lst[right_magnet]] != lst_magnet[magnet][right_lst[magnet]]):

                right_flag = direction * (-1)

        
    ############################################# 여기까지 왼쪽 오른쪽 돌리는 방향 정하기#####################

    ############ 아래부터는 실제로 돌리기 #################################################################

        if(direction == -1):

            left_lst[magnet] = (left_lst[magnet]+1) %8
            right_lst[magnet] = (right_lst[magnet]+1) %8
            red_lst[magnet] = (red_lst[magnet]+1) %8

        elif(direction == 1):

            left_lst[magnet] = (left_lst[magnet]-1) if left_lst[magnet] != 0 else 7 
            right_lst[magnet] = (right_lst[magnet]-1) if right_lst[magnet] != 0 else 7
            red_lst[magnet] = (red_lst[magnet]-1) if red_lst[magnet] != 0 else 7

        if(left_flag == -1):
            
            left_lst[left_magnet] = (left_lst[left_magnet]+1) if left_lst[left_magnet] != 7 else 0 
            right_lst[left_magnet] = (right_lst[left_magnet]+1) if right_lst[left_magnet] != 7 else 0
            red_lst[left_magnet] = (red_lst[left_magnet]+1) if red_lst[left_magnet] != 7 else 0
        
        elif(left_flag ==1):
            left_lst[left_magnet] = (left_lst[left_magnet]-1) if left_lst[left_magnet] != 0 else 7 
            right_lst[left_magnet] = (right_lst[left_magnet]-1) if right_lst[left_magnet] != 0 else 7
            red_lst[left_magnet] = (red_lst[left_magnet]-1) if red_lst[left_magnet] != 0 else 7

            
        if(right_flag == -1):
            left_lst[right_magnet] = (left_lst[right_magnet]+1) if left_lst[right_magnet] != 7 else 0 
            right_lst[right_magnet] = (right_lst[right_magnet]+1) if right_lst[right_magnet] != 7 else 0
            red_lst[right_magnet] = (red_lst[right_magnet]+1) if red_lst[right_magnet] != 7 else 0

        if(right_flag == 1):
            left_lst[right_magnet] = (left_lst[right_magnet]-1) if left_lst[right_magnet] != 0 else 7 
            right_lst[right_magnet] = (right_lst[right_magnet]-1) if right_lst[right_magnet] != 0 else 7
            red_lst[right_magnet] = (red_lst[right_magnet]-1) if red_lst[right_magnet] != 0 else 7


    score = 0

    for i in range(4):

        if(lst_magnet[i][red_lst[i]]==1):

            score += 2**(i)

    print(f"#{test_case} {score}")
    
    
    # first_left   = -1
    # first_right  = 2

    # second_left  = 6
    # second_right = 2

    # third_left   = 6
    # third_right  = 2

    # fourth_left  = 6
    # fourth_right = -1