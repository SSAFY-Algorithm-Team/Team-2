def solution(land):
    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    dp[0] = land[0]
    for i in range(1,n):
        for j in range(4):
            #i행 j열에 i-1행 j열과 겹치지 않는 선에서 max값 더하기
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if k!=j) 
    return max(dp[-1])