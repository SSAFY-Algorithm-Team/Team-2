# SWEA 4012 요리사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH# 소요시간: 45분 / 시도: 3회
# 소요시간: 20분 / 시도: 3회


T = int(input())
for test_case in range(1, T + 1):
    #일단 N을 2로 나눈 것 만큼 할당해야 하기 때문에
    # 한쪽을 고르면 나머지도 저절로 ?
    #그러면 일단 배열을 다시 만들어서 묶기
    #1,2 3,4  이렇게 한가지 2,3 1,4 한가지 1,4 2,3 한가지 
    #이렇게 N/2만큼 골라서 저장하게 되면 각자 차이가 나오게 되고 그 다음 가장 작은 것 구하면 될듯?
    #일단 그럼 N/2개 중복없이 뽑으면 되는데 dfs..?
    # →
    # 구현은 성공했지만 시간초과 뜸
    # →
    # 추가적으로 a에 0을 넣어서 고정시키고 start를 만들어 전체를 뽑는게 아니라 start에서부터 실행되게 해서 중복 없이 줄이는 식으로 구현했다.
    result =0
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    # print(arr)
    #a,b는 각자 식재료 뭐쓰는지임
    #a: 1,4
    #b: 2,3
    #처럼
    #각각 1,4 4,1 더하기
    def cook(a):
        suma = 0
        sumb = 0
        # b = []
        # for i in range(N):
        #     if i not in a:
        #         b.append(i)
        # print("요리중......")
        # print("cook1: ",a)
        # print("cook2: ",b)
        for i in range(N):
            for j in range(N):
                if i in a and j in a:
                    suma += arr[i][j]
                elif i not in a and j not in a:
                    sumb += arr[i][j]
        # for i in b:
        #     for j in b:
        #         sumb += arr[i][j]
        # print("cook a 맛: ",suma)
        # print("cook b 맛: ",sumb)
        return abs(suma-sumb)
    visit = [False]*N
    visit_cook = []
    min = [float('inf')]
    def dfs(start,count):
        if count >= N/2:
            # print("###########################")
            # print("요리 하나 결정 완료")
            m = cook(visit_cook)
            if min[0]>m:
                min[0] = m
            # print("맛 최소: ",min[0])
            return
        for i in range(start,N):
            if visit[i] == True:
                continue
            visit[i] = True
            visit_cook.append(i)
            dfs(i+1,count+1)
            visit_cook.pop()
            visit[i] = False
    
    visit_cook.append(0)
    dfs(1,1)
    result = min[0]
    print(f"#{test_case} {result}")