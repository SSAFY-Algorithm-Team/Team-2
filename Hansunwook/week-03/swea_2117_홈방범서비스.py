T = int(input())
for test_case in range(1, T + 1):
    result = 0
    N,M = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    # 초기 접근
    # K 만족하는지 확인하고 만족하는 최대 K 출력
    # 만족하는 범위의 집인지 확인하는 방법은 
    # -> 만약 a,b 중심일 경우 c,d에 집이 있으면 (a-c)^2+(b-d)^2 이 K^2 보다 작거나 같을 경우 안에 들어온다.
    # 그러므로 각 중심이 변할 떄 마다 업데이트 하고 해당되는 수를 센다
    houses = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 1]
    best = 0
    for r in range(N):
        for c in range(N):
            print("만약 중앙값이 ",r,c,"라면")
            dists = sorted(abs(r - i) + abs(c - j) for i, j in houses)
            print("거리: ", dists)
            # 거리 d를 포함하려면 K-1 >= d, 즉 K >= d+1
            for cnt in range(1, len(dists) + 1):
                # cnt번째로 가까운 집의 거리
                d = dists[cnt - 1]
                # 이 집을 포함하는 최소 K          
                K = d + 1                    
                cost = K * K + (K - 1) * (K - 1)
                profit = cnt * M - cost
                if profit >= 0 and cnt > best:
                    best = cnt
    result = best
    
    print(f"#{test_case} {result}")