T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = False
    R,C = map(int,input().split())
    arr = []
    for i in range(R):
        arr.append(list(map(input())))
    print(arr)
    #초기 접근
    # 일단 @에 접근 가능한지 여부를 따지면 됨
    # 시뮬레이션 돌리는데 문제는 이게 얼마나 돌려야 @에 닿는지 모른다는거
    # 일단 구현
    # 우상하좌
    udrl = [[0,1],[1,0],[-1,0],[0,-1]]
    def move_chang(move_key,move_vel):
        if move_key == "<":
            return 3
        elif move_key == ">":
            return 0
        elif move_key == "^":
            return 1
        elif move_key == "v":
            return 2
        elif move_key == "_":
            if move_vel == 0:
                return 0
            else:
                return 3
        elif move_key == "|":
            if move_vel == 0:
                return 2
            else:
                return 1
        # elif move_key == "?":
        #       return 
        number = arr[0][0]
        move_now = 0
        now = arr[0][1]
        i,j = 1,0
        while(1):
            if now == '@':
                result = True
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
            else:
                move_chang(now,number)
            # now = arr[][]
                
    print(f"#{test_case} {result}")