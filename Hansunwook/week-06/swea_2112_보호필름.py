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
    tf = [False]
    min_count = [K]
    count = [0]


    # #만족하는지 확인하는 함수임
    # def check(arr):
    #     #일단 체크해야하는거 뒤집고 확인
    #     arr_90 = list(zip(*arr))
    #     for i in arr_90:
    #         tf = check_one(i)
    #         if tf == False:
    #             return False
    #     return True

    # def check_one(arr):
    #     a = arr[0]
    #     count = 0
    #     for j in arr:
    #         if count >= K:
    #             return True
    #         if a == j:
    #             count += 1
    #         else:
    #             count = 1
    #             a = j
    #     return False

    def check1(arr_90,c):

            if(K==1):
                return True
            
            rune=1

            for row in range(1,D):
                if(arr_90[row][c]==arr_90[row-1][c]):
                    rune+=1
                    if(rune==K):
                        return True

                else:
                    rune=1

            return False

    def check(arr):

        return all(check1(arr,c) for c in range(W))



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

        # 배열 밖에서 선언하면 시간 좀 줄어듬 굳이 안에서 복사할 필요 없음
        # 그리고 복사는 전부 말고 딱 한줄만 복사해서 되돌리기 
        original=arr[c][:]
        for i in range(2):
            arr[c] =  [i]*W
            count[0] += 1
            dfs(c+1)
            count[0] -= 1
            arr[c] =  original[:]
        dfs(c+1)

    if check(arr):
        result = 0
    else:
        dfs(0)
        result = min_count[0]

    print(f"#{test_case} {result}")