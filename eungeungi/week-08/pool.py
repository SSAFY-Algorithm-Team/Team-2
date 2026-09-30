def pool(d,m,q,y,c):
    dp = [0] * 13 
    for i in range(1,13):
        dp[i] = dp[i-1] + min(d * c[i-1] , m)
        if i>=3:
            dp[i] = min(dp[i-3]+q , dp[i])
        else:
            dp[i] = min(dp[i],q)
    return min(dp[12],y)
T = int(input())
for tc in range(1,T+1):
    d,m,q,y = map(int,input().split())
    c = list(map(int,input().split()))
    ans = pool(d,m,q,y,c)
    print(f"#{tc} {ans}")