T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 초기 접근
    # 일단 맛이 최대가 되면서 조건 만족해야 함
    # 그러면 먼저 맛이 최대 되는 조합 찾기?
    # dfs?
    result = 0
    N,L = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    visit = [False]*N
    max = [0]
    sum = [0]
    to_arr = []
    def dfs(start,add,sub):
        #추가로 끝까지 돌았지만 넘지 않아 업데이트 되지 않는 문제를 해결
        if start >= N and add <= L:
            tast = sum[0]
            # print("########햄버거 하나")
            # print("맛: ", tast)
            # print("토핑: ",to_arr)
            if max[0] < tast:
                max[0] = tast
                # print("맛 업데이트")
        if add > L:
            tast = sum[0] - sub
            # print("########햄버거 하나")
            # print("맛: ", tast)
            # print("토핑: ",to_arr)
            if max[0] < tast:
                max[0] = tast
                # print("맛 업데이트")
            return
        for i in range(start, N):
            # print("토핑 추가중....")
            # print("토핑: ",i)
            sum[0] += arr[i][0]
            to_arr.append(i)
            dfs(i+1,add + arr[i][1], arr[i][0])
            # print("토핑 빼기--------",i)
            to_arr.pop()
            sum[0] -= arr[i][0]
    dfs(0,0,0)
    result = max[0]
    print(f"#{test_case} {result}")