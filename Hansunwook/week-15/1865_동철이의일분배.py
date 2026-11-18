T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    P = []
    result_max = [-1]
    visit = [False]*N
    for i in range(N):
        P.append(list(map(int,input().split())))
    def dfs(count,per):
        if count >=N:
            if per > result_max[0]:
                result_max[0] = per
            return
        for i in range(N):
            if visit[i]:
                continue
            visit[i] = True
            dfs(count+1, per*P[count][i]/100)
            visit[i] = False
    dfs(0,1)
    print(f"#{test_case} {result_max[0]}")