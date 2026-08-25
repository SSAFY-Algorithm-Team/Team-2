
# 등굣길 프로그래머스
# 웅덩이를 통해서 오는길, 웅덩이를 거치는 길을 모두 제외하며 dp실시하면 됨.
# 나눗셈의 크기가 클 때 내장함수 divmod를 사용

def solution(m, n, puddles):
    dp = [[1] * (m) for  _ in range(n)]
    
    for puddle in puddles: # 웅덩이 처리
        x, y = puddle[1] - 1, puddle[0] - 1
        if x == 0:
            for k in range(y, m):
                dp[x][k] = 0
        elif y == 0:
            for k in range(x, n):
                dp[k][y] = 0
        else:
            dp[x][y] = 0
    #print(dp)
        
    for x in range(1, n):
        for y in range(1, m):
            if dp[x][y] == 0:
                continue
            _, dp[x][y] = divmod(dp[x-1][y] + dp[x][y-1], 1000000007)
    # print(dp)
    answer = dp[n-1][m-1]
    # print(answer)
    return answer