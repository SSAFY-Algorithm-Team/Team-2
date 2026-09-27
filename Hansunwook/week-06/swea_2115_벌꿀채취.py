T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    # 
    N,M,C = map(int,input().split())
    ori_arr = []
    for i in range(N):
        ori_arr.append(list(map(int,input().split())))
    #일단 개수가 작기 때문에
    # 전부 탐색해서 배열로 만든 다음
    # 겹치지 않고 가장 높게 두개 고르면 되지 않을까

    # 추가적으로 전부 탐색할 경우 채취하는 것도 가장 큰걸 선택해야 하기 때문에 
    # 그것도 돌려서 가장큰걸로 저장해야함

    h_arr = []
    for i in range(N):
        h_arr.append([0]*N)
    def h_update(arr):
        n = len(arr)
        max_h = 0

        def dfs(idx, total, hon):
            nonlocal max_h
            if idx == n:
                if total <= C and hon > max_h:
                    max_h = hon
                return
            # idx번째 벌통을 채취하는 경우
            dfs(idx + 1, total + arr[idx], hon + arr[idx] * arr[idx])
            # idx번째 벌통을 채취 안 하는 경우
            dfs(idx + 1, total, hon)
        dfs(0, 0, 0)
        return max_h

    
    for i in range(N):
        for j in range(0,N-M+1):
            # print("##########",i,j)
            arr = list(ori_arr[i][j:j+M])
            # print("시작",h_arr[i][j])
            h_arr[i][j] = h_update(arr)
    # print(h_arr)
    max_h = -1
    for i in range(N):
        for j in range(0,N-M+1):
        #    print("i,j",i,j)
           for k in range(N):
                for h in range(N-M+1):
                    if k > i or h >= j+M:
                        # print("k,h",k,h)
                        sum_h = h_arr[i][j] + h_arr[k][h]
                        if max_h < sum_h:
                            # print("업데이트: ",sum_h)
                            # print(i,j)
                            # print(k,h)
                            max_h = sum_h
    result = max_h
    print(f"#{test_case} {result}")