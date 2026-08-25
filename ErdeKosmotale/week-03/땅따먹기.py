#땅따먹기 프로그래머스

#행 별로 한 번만 못밟는다는 점에서 dp로 어렵지 않게 풀림.

def solution(land):
    #한번만 못밟는거임 ㅋㅋ
    
    answer = 0

    n=len(land)
    
    dp=[[0]*len(land[0]) for _ in range(n)]
    
    for i in range(4):
        dp[0][i]=land[0][i]
    
    for row in range(1,n):
        for col in range(4):
            t_max=0
            for i in range(4):
                if(col==i):
                    continue
                
                t_max=max(t_max,dp[row-1][i])
            
            dp[row][col]=(t_max+land[row][col])
    
    answer=max(dp[n-1])            
    
    return answer