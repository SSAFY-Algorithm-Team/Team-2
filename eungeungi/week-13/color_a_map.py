def color_map(N, color, connection):
    mini = float('inf')
    selected = [0] * N

    def dfs(idx, cnt):
        nonlocal mini

        if cnt >= mini:
            return

        if idx == N:
            mini = min(mini, cnt)
            return
        # 색깔 1~4중 하나씩 부여
        for c in range(1, 5):
            flag = True
            # i번째 인덱스의 색깔을 결정
            for i in range(idx):
                # 인접한 나라가 같은 색인 경우 색 변경
                if connection[idx][i] == 1 and selected[i] == c:
                    flag = False
                    break
            #색깔이 안 겹친다면
            if flag:
                # 현재 인덱스의 색깔 결정
                selected[idx] = c

                # 주어진 색깔과 겹친다면 idx만 늘리기
                if color[idx] == c:
                    dfs(idx + 1, cnt)
                # 주어진 색깔과 다르다면 색을 바꿨으니 cnt도 추가
                else:
                    dfs(idx + 1, cnt + 1)
                # 색 초기화
                selected[idx] = 0

    dfs(0, 0)
    return mini
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    color = list(map(int, input().split()))
    connection = []
    for _ in range(N):
        row = list(map(int,input().split()))
        connection.append(row)
    ans = color_map(N,color,connection)
    print(f"#{tc} {ans}")