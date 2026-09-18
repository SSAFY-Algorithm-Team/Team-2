T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    result = 0
    # 먼저 D,W가 적기 때문에 완탐?
    # ㅠㅠ ㅠ
    # 생각 안나서 클로드한테 어떻게 풀어야 할지 물어봄
    # 일단 check함수 만들어서 연속된거 있는지 아닌지 확인하는 함수 만든 다음에
    # 모든 줄이 적용안함, A, B 이렇게 3개로 나눠져 있기 때문에 
    # 전부 모든 줄마다 적용해보는 그리고 최소 개수 구하는
    # 그런 함수를 짜야한다고 했음
    # 그래서 그거 그대로 구현해보기 
    # D = 세로, W = 가로, K = 합격기준  
    D,W,K = map(int,input().split())
    arr = []
    for i in range(D):
        arr.append(list(map(int,input().split())))

    #만족하는지 확인하는 함수임
    def check(arr):
        #일단 체크해야하는거 뒤집고 확인
        arr_90 = list(zip(*arr))
        for i in arr_90:
            a = i[0]
            count = 0
            tf = False
            for j in i:
                if count >= K:
                    tf = True
                    continue
                if a == j:
                    count += 1
                else:
                    count = 1
                    a = j
            if tf == False:
                return tf
        return tf
    tf = [False]
    min_count = [K]
    count = [0]
    #dfs로 전부 방문하고 돌아오는 코드임
    def dfs(c):
        #가지치기
        if min_count[0] <= count[0]:
            return
        if c >= D:
            if check(arr):
                if min_count[0] > count[0]:
                    min_count[0] = count[0]
            return
        for i in range(2):
            arr2 = arr[:]
            arr[c] =  [i]*W
            count[0] += 1
            dfs(c+1)
            count[0] -= 1
            arr[c] =  arr2[c]
        dfs(c+1)

    if check(arr):
        result = 0
    else:
        dfs(0)
        result = min_count[0]

    print(f"#{test_case} {result}")