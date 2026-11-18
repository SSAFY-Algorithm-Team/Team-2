def find(N,M,arr):
    cnt = 0

    def dfs(idx,total):
        nonlocal cnt
        if total ==M:
            cnt +=1
            return
        if idx ==N or total >M:
            return
        
        dfs(idx+1,total+arr[idx])
        dfs(idx+1,total)
    dfs(0,0)
    return cnt

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = find(N,M,arr)
    print(f"#{tc} {ans}")