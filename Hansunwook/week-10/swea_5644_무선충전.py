T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    # 이동하는 곳은 정해져 있고 그 경로대로 따라가서 최대로 충전할 수 있는 곳을 정하는 문제
    # 그냥 전부 계산해서 제일 큰곳 print 하면 되는 간단한 문제인가?
    # 추가적으로 겹치면 나눠져서 만약 둘다 같은 충전소밖에 없으면 나눠가지고
    # 각각 두개 밟고 있으면 그냥 큰거 두개 합치기
    # 일단 구현
    M,A = map(int,input().split())
    A_move = list(map(int,input().split()))
    B_move = list(map(int,input().split()))
    #위치
    APD = []
    #C
    APC = []
    #P 
    APP = []
    for i in range(A):
        x,y,c,p = map(int,input().split())
        APD.append([x,y])
        APC.append(c)
        APP.append(p)
    move = [[0,0],[0,-1],[1,0],[0,1],[-1,0]]          # ✅ [dx,dy] 정지,상,우,하,좌

    def cel(A_x,A_y,B_x,B_y):
        #max 안될까봐 일단 0 넣어놓음
        # 되는지 안되는지는 물어봐야지
        Battery_A = [-1]                               # ✅ BC 번호 저장, -1 = 접속 안 함
        Battery_B = [-1]                               # ✅
        for i in range(A):
            # 해당되면 넣는건데..
            # A가 해당되는걸 B에도 넣을 필요가 있을까....
            # 없는 것 같기도 일단 continue로 안넣기
            # ✅ → 넣어야 함, continue 삭제
            if APC[i] >= abs(A_x - APD[i][0])+ abs(A_y - APD[i][1]):   # ✅ [0] → [1]
                Battery_A.append(i)                                     # ✅ P 대신 번호
            if APC[i] >= abs(B_x - APD[i][0])+ abs(B_y - APD[i][1]):   # ✅ [0] → [1]
                Battery_B.append(i)                                     # ✅
        # ✅ 모든 (A 선택, B 선택) 조합 비교
        best = 0
        for a in Battery_A:
            for b in Battery_B:
                if a == b:                             # ✅ 같은 BC면 나눠 가져도 합은 P 하나
                    total = APP[a] if a != -1 else 0
                else:
                    total = 0
                    if a != -1:
                        total += APP[a]
                    if b != -1:
                        total += APP[b]
                best = max(best, total)
        return best                                    # ✅
    A_x = 1                                            # ✅ 0 → 1
    A_y = 1                                            # ✅ 0 → 1
    B_x = 10
    B_y = 10
    result += cel(A_x,A_y,B_x,B_y)                     # ✅ 0초 충전
    for i in range(M):
        A_x += move[A_move[i]][0]
        A_y += move[A_move[i]][1]
        B_x += move[B_move[i]][0]
        B_y += move[B_move[i]][1]
        result += cel(A_x,A_y,B_x,B_y)                 # ✅ 범위 체크 if 삭제, 디버그 print 삭제
        
    print(f"#{test_case} {result}")