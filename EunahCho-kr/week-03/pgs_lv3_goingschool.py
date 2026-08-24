# 프로그래머스 Lv3. 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 소요시간 2h / 시도 횟수 : ? 

# 접근 방식 블로그 도움 받음 
# 앞으론 row col쓰기,,,,,,,,,,,


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

# 감자 코드

# def solution(m, n, puddles):
#     dp = [[0] * (m + 1) for  _ in range(n + 1)]
    
#     for col,row in puddles:
        
#         dp[row][col]=-1
    
#     dp[1][1]=1
    
#     for row in range(1, n + 1):
#         for col in range(1, m + 1):
            
#             if(dp[row][col]==-1):
#                 continue
            
#             if(dp[row-1][col]!=-1):
#                 #dp[row][col]+= dp[row-1][col]%1000000007
#                 _, dp[row][col]= divmod(dp[row-1][col] + dp[row][col], 1000000007)
#             if(dp[row][col-1]!=-1):
#                 #dp[row][col]+= dp[row][col-1]%1000000007
#                 _, dp[row][col]= divmod(dp[row][col-1] + dp[row][col], 1000000007)
    
#     # print(dp)
#     answer = dp[n][m]

#     return answer