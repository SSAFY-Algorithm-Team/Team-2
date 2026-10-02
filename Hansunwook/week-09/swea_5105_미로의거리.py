T = int(input())
from collections import deque
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    arr = []
    start = []
    end = []
    for i in range(N):
        arr.append(list(map(int,input())))
        for j in range(N):
            if arr[i][j] == 2:
                start.append([i,j,0])
    # 0은 통로, 1은 벽, 2는 출발, 3은 도착
    #bfs 구현
    queue = deque()
    udrl = [[0,1],[1,0],[-1,0],[0,-1]]
    visit = []
    for i in range(N):
        visit.append([False]*N)
    finish = [False]
    queue.append(start[0])
    # print(queue)
    while(queue):
        if finish[0]:
            break
        nowa,nowb,nowc = queue.popleft()
        visit[nowa][nowb] = True
        # print("#####",nowa,nowb,"는 지금 좌표임 ",nowc,"만큼 왔음")
        for i in range(4):
            # print("이동중...")
            nexta = nowa + udrl[i][0]
            nextb = nowb + udrl[i][1]
            if 0 <= nexta < N and 0 <= nextb < N:
                if arr[nexta][nextb] == 1 or visit[nexta][nextb]:
                    # print("x")
                    continue
                if arr[nexta][nextb] == 0:
                    # print("이동 가능!!!",nexta,nextb)
                    queue.append([nexta,nextb,nowc+1])
                    visit[nexta][nextb] = True
                if arr[nexta][nextb] == 3:
                    # print("######도착 완료")
                    result = nowc
                    visit[nexta][nextb] = True
                    finish[0] = True
    print(f"#{test_case} {result}")