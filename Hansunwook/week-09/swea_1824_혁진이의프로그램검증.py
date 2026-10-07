T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.   

for test_case in range(1, T + 1):
    #초기 접근
    # 일단 @에 접근 가능한지 여부를 따지면 됨
    # 시뮬레이션 돌리는데 문제는 이게 얼마나 돌려야 @에 닿는지 모른다는거......
    # -> (위치, 방향, 메모리) 상태가 반복되면 무한루프이므로 visited로 끊음

    
    result = "NO"
    R,C = map(int,input().split())
    arr = []
    for i in range(R):
        arr.append(list(input()))
    # 우하상좌 (0:우, 1:하, 2:상, 3:좌)
    udrl = [[0,1],[1,0],[-1,0],[0,-1]]

    def move_chang(move_key, move_vel, move_now):
        if move_key == "<":
            return 3
        elif move_key == ">":
            return 0
        elif move_key == "^":
            return 2 
        elif move_key == "v":
            return 1      
        elif move_key == "_":
            if move_vel == 0:
                return 0
            else:
                return 3
        elif move_key == "|":
            if move_vel == 0:
                return 1
            else:
                return 2
        return move_now    
    
    # 4차원 visited [행][열][방향][메모리]
    visited = []
    for i in range(R):                  # 행
        row = []
        for j in range(C):              # 열
            cell = []
            for d in range(4):          # 방향
                cell.append([False] * 16)   # 메모리 0~15
            row.append(cell)
        visited.append(row)
    stack = [(0, 0, 0, 0)]
    visited[0][0][0][0] = True

    while stack:
        i, j, move_now, number = stack.pop()
        now = arr[i][j]
        if now == '@':
            result = "YES"
            break
        elif now == '-':
            if number <= 0:
                number = 15
            else:
                number -= 1
        elif now == '+':
            if number >= 15:
                number = 0
            else:
                number += 1
        elif now.isdigit():
            number = int(now)
        else:
            move_now = move_chang(now, number, move_now)

        # ?면 4방향 전부, 아니면 현재 방향 하나
        if now == '?':
            next_dirs = [0, 1, 2, 3]
        else:
            next_dirs = [move_now]

        for d in next_dirs:
            ni = (i + udrl[d][0]) % R      # 격자 밖이면 반대편으로
            nj = (j + udrl[d][1]) % C
            if not visited[ni][nj][d][number]:
                visited[ni][nj][d][number] = True
                stack.append((ni, nj, d, number))

    print(f"#{test_case} {result}")