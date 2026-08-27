def solution(m, n, puddles):
    m, n = n, m
    dp = [[0]*m for _ in range(n)]
    for i in range(len(puddles)):
        x, y = puddles[i]
        dp[x-1][y-1] = -1
    
    for i in range(n):
        if dp[i][0] == 0:
            dp[i][0]+=1
        else:
            break
    for j in range(1,m):
        if dp[0][j] ==0:
            dp[0][j] +=1
        else:
            break
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != -1:
                
                if dp[i-1][j] != -1 and dp[i][j-1] != -1:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
                    
                elif dp[i-1][j] != -1 and dp[i][j-1] == -1:
                    dp[i][j] = dp[i-1][j] % 1000000007
                    
                elif dp[i][j-1] != -1 and dp[i-1][j] == -1:
                    dp[i][j] = dp[i][j-1] % 1000000007
                
                else:
                    dp[i][j] = 0
            
                    
    return dp[n-1][m-1]

