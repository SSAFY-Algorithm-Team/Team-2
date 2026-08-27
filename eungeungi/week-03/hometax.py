#운영 비용 1+4(1+2+...+(n-1))
# 1 + 4 * n(n-1)/2 = 2n^2-2n+1
def find(arr,M):
    N = len(arr)
    cost = [0] + [2*(n**2) -2*n + 1 for n in range(1,N+2)]

    # 집 위치 저장
    houses = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] ==1:
                houses.append((r,c))
    answer =  0

    # 서비스 중심 위치
    for r in range(N):
        for c in range(N):

            # 1부터 N+1까지 확인
            for k in range(1,N+2):
                cnt = 0

                # 현재 중심, 현재 k에서 포함되는 집 개수 세기
                for hr, hc in houses:
                    d = abs(r-hr) + abs(c-hc)

                    if d < k:
                        cnt +=1

                # 손해 보지 않으면 최대 집 수 갱신
                if cnt * M >= cost[k]:
                    answer = max(answer, cnt)
    return answer

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        row = list(map(int,input().split()))
        arr.append(row)
    ans = find(arr,M)
    print(f"#{tc} {ans}")