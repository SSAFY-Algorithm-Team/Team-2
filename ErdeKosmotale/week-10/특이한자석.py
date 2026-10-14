
# 자석 2번이 오른쪽 6번이 왼쪽 빨간색이 0번으로 시작
# 시계방향으로 돌면 현재 있는 자석이 좌표가 작아지는 방향으로 됨
# 반시계방향으로 돌면 현재있는 자석이 좌표가 커지는 방향으로 감
# 시계방향 1 반시계방향 -1

def dfs(num_magnet,direction):

    if(num_magnet==-1 or num_magnet == 4):
        return

    # if visited[num_magnet]:
    #     return

    visited[num_magnet] = True

    left_magnet = num_magnet - 1
    right_magnet = num_magnet + 1

    now_left  = lst_magnet[num_magnet][left_right_red[num_magnet][0]]
    now_right = lst_magnet[num_magnet][left_right_red[num_magnet][1]]

    if(direction == 1):

        left_right_red[num_magnet][0] = left_right_red[num_magnet][0] -1 if left_right_red[num_magnet][0]!=0 else 7
        left_right_red[num_magnet][1] = left_right_red[num_magnet][1] -1 if left_right_red[num_magnet][1]!=0 else 7
        left_right_red[num_magnet][2] = left_right_red[num_magnet][2] -1 if left_right_red[num_magnet][2]!=0 else 7

    else:
         
        left_right_red[num_magnet][0] = left_right_red[num_magnet][0] +1 if left_right_red[num_magnet][0]!=7 else 0
        left_right_red[num_magnet][1] = left_right_red[num_magnet][1] +1 if left_right_red[num_magnet][1]!=7 else 0
        left_right_red[num_magnet][2] = left_right_red[num_magnet][2] +1 if left_right_red[num_magnet][2]!=7 else 0

    

    if(left_magnet>=0):

        left_right = lst_magnet[left_magnet][left_right_red[left_magnet][1]] # 왼쪽 자석의 오른쪽 부분

        if(left_right != now_left and not visited[left_magnet]):
            dfs(left_magnet,direction*(-1))


    if(right_magnet < 4):

        right_left = lst_magnet[right_magnet][left_right_red[right_magnet][0]]

        if(right_left != now_right and not visited[right_magnet]):
            dfs(right_magnet, direction * (-1))


    

        
T = int(input())


for test_case in range(1 , T + 1):

    K = int(input())  # 자석 돌리는 총 수

    lst_magnet = []
    for _ in range(4):

        lst_magnet.append(list(map(int,input().split())))


    #lst_magnet = [list(map(int,input().split)) for _ in range(4)]

    left_right_red = [[6,2,0] for _ in range(4)]

    for _ in range(K):

        magnet_now, direction = map(int,input().split())

        magnet_now -=1

        visited= [0]*4
     

        
        dfs(magnet_now,direction)

    score = 0

    for num_magnet in range(4):

        if(lst_magnet[num_magnet][left_right_red[num_magnet][2]]== 1):

            score += 2**(num_magnet)

    print(f"#{test_case} {score}")

