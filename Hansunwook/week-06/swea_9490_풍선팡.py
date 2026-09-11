
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    #
    rlud = [[1,0],[0,1],[-1,0],[0,-1]]
    N,M = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    def sum_pop(a,b):
        a2 = a
        b2 = b
        sum_p = arr[a][b]
        for i in range(4):
            a2 = a + rlud[i][0]
            b2 = b + rlud[i][1]
            for j in range(arr[a][b]):    
                if 0<=a2<N and 0<=b2<M:
                    # print("add",arr[a2][b2],a2,b2)
                    sum_p += arr[a2][b2]
                    a2 += rlud[i][0]
                    b2 += rlud[i][1]
        return sum_p
    max = -1 
    for i in range(N):
        for j in range(M):
            # print("########",i,j)
            result = sum_pop(i,j)
            # print(result)
            if max < result:
                # print("!!!!!!!")
                max = result
    print(f"#{test_case} {max}")