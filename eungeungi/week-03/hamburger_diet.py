def ham(arr,L):
    n = len(arr)
    maxi = 0

    def dfs(idx,score,calorie):
        if calorie>L:
            return
        if idx == n:
            nonlocal maxi
            maxi = max(maxi,score)

        dfs(idx+1,score+arr[idx][0],calorie+arr[idx][1])

        dfs(idx+1,score,calorie)
    dfs(0,0,0)
    return maxi
T = int(input())
for tc in range(1,T+1):
    N, L = map(int, input().split())
    arr = []
    for _ in range(N):
        row = list(map(int,input().split()))
        arr.append(row)
    ans = ham(arr,L)
    print(f"#{tc} {ans}")