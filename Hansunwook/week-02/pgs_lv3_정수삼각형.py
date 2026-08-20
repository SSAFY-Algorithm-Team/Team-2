def solution(triangle):
    answer = 0
    # 초기 접근
    # 먼저 음.... 아래에서 시작해서
    # 위로 올라가서 밑에서 두개중 큰거 올려주는식으로?
    N = len(triangle)
    result = [0]
    #맨 밑에서 바로 위에 부분부터 시작 
    count = N-2
    #저장용 배열?
    arr = triangle[N-1]
    #밑에서부터 위까지 돌리기
    while(count >= 0):
        # print(count,"위치 시작")
        # print(triangle[count])
        for i in range(len(triangle[count])):
            triangle[count][i] += max(triangle[count+1][i],triangle[count+1][i+1])
            # print("큰 부분 저장")
        count -= 1
    # print(triangle)
    answer = int(triangle[0][0])
    
    return answer