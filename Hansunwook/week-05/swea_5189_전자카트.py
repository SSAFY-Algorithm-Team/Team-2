T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    #초기 접근: 
    # 그냥 123 있으면 1231 이렇게 하는거라는건가?
    # 1234 있으면 12341에서 234 섞으라는거?
    # 이렇게 이해했다면 일단 먼저 이렇게 구현해서 
    # dfs로 중복 없이 돌리고 제일 작은 수 업데이트 시키기
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    min_count = [float("inf")]
    use_count = [0]
    visit = [False]*N
    def dfs(count,a):
        if count >= N:
            use_count[0] += arr[a][0]
            # print("###############청소 하나 완료")
            # print("배터리 소모량: ",use_count[0])
            if min_count[0] > use_count[0]:
                # print("가장 작은 배터리소비량 업데이트")
                min_count[0] = use_count[0]
            use_count[0] -= arr[a][0]
            return
        for i in range(1,N):
            if visit[i]:
                continue
            visit[i] = True
            b=i
            # print("청소중...",a+1,b+1)
            # print("더하는중...",use_count[0],arr[a][b])
            use_count[0] += arr[a][b]
            dfs(count+1,b)
            visit[i] = False
            use_count[0] -= arr[a][b]
    dfs(1,0)
    result = min_count[0]
    print(f"#{test_case} {result}")