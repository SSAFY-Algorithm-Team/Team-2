# 이렇게 푸는건 처음 보네.. 함수값이 계속 호출되기에 
# 99 값이 1을 반환하고 그 dfs를 호출한 함수들이 각각 1로 저장되는 방식
def find(N,M,g):
    v = [False] * 100
    def dfs(idx):
        
        if idx == 99:
            return 1
        v[idx] = True


        for elem in g[idx]:
            if not v[elem]:
                if dfs(elem) ==1:
                    return 1
        return 0
    return dfs(0)


T = 10
for tc in range(1,T+1):
    N, M = map(int, input().split())
    g = [[] for _ in range(100)]
    data = list(map(int, input().split()))
    for i in range(0,M*2,2):
        g[data[i]].append(data[i+1])

    ans = find(N,M,g)
    print(f"#{tc} {ans}")

# 찾는 순간 ans에 1 값 반영 후 추가 탐색 종료조건 같이 있어서 그대로 끝
def find(N, M, g):
    v = [False] * 100
    ans = 0

    def dfs(idx):
        nonlocal ans

        if idx == 99:
            ans = 1
            return

        v[idx] = True

        for elem in g[idx]:
            if not v[elem] and ans == 0:
                dfs(elem)

    dfs(0)
    return ans