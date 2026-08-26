def solution(m, n, puddles):
    #초기 접근
    # 일단 웅덩이인 경우만 피해서 가는 최단경로이니까
    # 위나 왼쪽으로 돌아가지만 않으면 최단일 것 같은데..
    # 그러면 각 좌표마다 -1-1 한거 더한게 지금 경로 숫자
    # 그리고 웅덩이면 0 처리 
    arr = []
    for i in range(n):
        arr.append([0]*m)
    # print(arr)
    for i in range(0,n):
        for j in range(0,m):
            if i==0 and j==0:
                arr[i][j] = 1
                continue
            # 이 웅덩이 좌표 때문에 계속 틀림....문제 잘보기 좌표 확실히 잡고 가기
            # 변수 설정 제대로 하기 
            if [j+1,i+1] in puddles:
                # print("웅덩이: ",i,j)
                arr[i][j] = 0
            elif i == 0:
                arr[i][j] = arr[i][j-1]
            elif j == 0:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    answer = arr[n-1][m-1] % 1000000007
    # print(arr)
    return answer