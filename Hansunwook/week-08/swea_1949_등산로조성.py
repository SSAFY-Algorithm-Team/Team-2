T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = [0]
    N,K = map(int,input().split())
    arr = []
    top = 0
    visit = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
        visit.append([False]*N)
        if top < max(arr[i]):
            top = max(arr[i])
    top_point = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:
                top_point.append([i,j])
    udrl = [[0,1],[0,-1],[1,0],[-1,0]]
    notreduce = [True]
    # print(top)
    # print(top_point)
    #최대 K깎을 수 있는거 구현..
    # -> 얼마나 깎는지는 신경 안쓰고 그냥 차이보다 +1 정도 더 깎기?
    def dfs(nowa,nowb,count):
        nexta = nowa
        nextb = nowb
        # print(nowa,nowb,"에서 이동중.. >")
        for i in range(4):
            nexta = nowa + udrl[i][0]
            nextb = nowb + udrl[i][1]
            if not (0<=nexta<N and 0<=nextb<N):
                continue
            if visit[nexta][nextb]:
                continue

            if arr[nowa][nowb] > arr[nexta][nextb]:
                # print("> 이동 성공:",nexta,nextb)
                visit[nexta][nextb] = True
                dfs(nexta,nextb,count+1)
                visit[nexta][nextb] = False
            else:
                #다음과 지금의 차이
                diff = arr[nexta][nextb]-arr[nowa][nowb]
                if notreduce[0] and K >= (diff+1):
                    # print("> 깎아서 이동 완료..:",nexta,nextb)
                    visit[nexta][nextb] = True
                    arr[nexta][nextb] -= (diff+1) 
                    notreduce[0] = False
                    dfs(nexta,nextb,count+1)
                    arr[nexta][nextb] += (diff+1) 
                    notreduce[0] = True
                    visit[nexta][nextb] = False
        #다끝나서 이제 못돌리면 count 비교
        # print("#######이제 돌릴거 없음")
        # print(count,"만큼 돌았음")
        if count > result[0]:
            # print("########바뀜!!!")
            result[0] = count
        count = 0
        return
    
    for a,b in top_point:
        visit[a][b] = True
        dfs(a,b,1)
        visit[a][b] = False
    
    print(f"#{test_case} {result[0]}")