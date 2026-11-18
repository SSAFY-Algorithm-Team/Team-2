T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = [0]
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #dfs로 풀기
    def dfs(count,sum):

        if sum > K:
            return
        if sum == K:
            result[0] += 1
            return
        if count >= N:
            return        
        for i in range(count,N):
            dfs(i+1,sum + A[i])
    dfs(0,0)
    print(f"#{test_case} {result[0]}")