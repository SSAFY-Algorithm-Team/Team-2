def check(D,W,K,arr):
    for col in range(W):

        if K == 1:
            return True
        
        cnt = 1
        if cnt >=K:
            return True

        for row in range(1,D):
            if arr[row][col] == arr[row-1][col]:
                cnt+=1
            else:
                cnt = 1

            if cnt >=K:
                break

        if cnt<K:
            return False
    return True

def dfs(D,W,K,arr,idx,cnt,ans):
    # 현재 순회하는 값이 ans 이상이면 더 볼 이유가 없음
    if cnt >= ans:
        return ans
    # 전체를 다시 순회하고 최소값 갱신
    if check(D,W,K,arr):
        return min(ans,cnt)
    # 마지막 행을 본 경우는 이미 A와 B를 다 바꿔본 상태 
    if idx == D:
        return ans

    # 기존 행 정보 저장
    origin = arr[idx][:]

    # 안 채우고 순회
    ans = dfs(D,W,K,arr,idx+1,cnt,ans)
    # A값 채우기 후 순회
    arr[idx] = [0] * W
    ans = dfs(D,W,K,arr,idx+1,cnt+1,ans)

    # B값 채우기 후 순회
    arr[idx] = [1] * W
    ans = dfs(D,W,K,arr,idx+1,cnt+1,ans)

    arr[idx] = origin

    return ans

    

T = int(input())
for tc in range(1,T+1):
    D, W, K = map(int,input().split())
    arr = []
    for _ in range(D):
        row = list(map(int,input().split()))
        arr.append(row)
    ans = K
    ans = dfs(D,W,K,arr,0,0,ans)
    print(f"#{tc} {ans}")