# 3번째, 7번째,3번째,7번째가 맞닿아 있음
# rotate에 저장된 값 하나씩 빼
# rotate[0]값을 돌릴 때 인접 톱니바퀴먼저 확인 
from collections import deque
def find(mag,rotate):
    d = [0] * 4
    for idx, dir in rotate:
        d[idx] = dir
        # 왼쪽 먼저 확인
        for i in range(idx-1,-1,-1):
            if mag[i][2] != mag[i+1][6]:
                d[i] = d[i+1] * -1
            else:
                break
        # 오른쪽 확인
        for i in range(idx+1,4):
            if mag[i-1][2] != mag[i][6]:
                d[i] = d[i-1] * -1
            else:
                break
        # 방향 정해졌으면 1칸씩 이동
        for i in range(4):
            if d[i] !=0:
                mag[i].rotate(d[i])
        # 한 번 회전 끝났으면 d 초기화
        d = [0]*4
    answer = 0
    for i in range(4):
        if mag[i][0] == 1:
            answer += 2**i
    return answer



T = int(input())
for tc in range(1,T+1):
    K = int(input())
    mag = []
    for _ in range(4):
        row = deque(map(int,input().split()))
        mag.append(row)
    rotate = []
    for i in range(K):
        idx,dir = map(int,input().split())
        rotate.append((idx-1,dir))
    ans = find(mag,rotate)
    print(f"#{tc} {ans}")