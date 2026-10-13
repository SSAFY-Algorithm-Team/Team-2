# 4013. [모의 SW 역량테스트] 특이한 자석
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH&categoryId=AWIeV9sKkcoDFAVH&categoryType=CODE&problemTitle=4013&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&


"""
하나의 자석이 1 칸 회전될 때, 붙어 있는 자석은 서로 붙어 있는 날의 자성과 다를 경우에만 인력에 의해 반대 방향으로 1 칸 회전된다.

모든 회전이 끝난 후 점수
- 1 번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N 극 : 0 점, S 극 : 1 점
- 2 번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N 극 : 0 점, S 극 : 2 점
- 3 번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N 극 : 0 점, S 극 : 4 점
- 4 번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N 극 : 0 점, S 극 : 8 점

4 개 자석의 자성 정보와 자석을 1 칸씩 K 번 회전시키려고 할 때, K 번 자석을 회전시킨 후 획득하는 점수의 총 합을 출력
"""
import sys
from collections import deque
sys.stdin = open('4013_input.txt')


def solve(k, magnets, cmds):

    # cmds를 돌면서
    for idx, rot in cmds:
        # 돌리기 전에 현재 마그넷의 2, 6 인덱스들 확인 (1번자석의 6, 4번 자석의 2는 제외)
        flag = [False] * 4
        for i in range(2):
            # 극이 다르다면 -> 같이 돌 애 -> 플래그
            if magnets[i][2] != magnets[i + 1][6]:
                flag[i] = flag[i + 1] = True
 
        magnets[idx - 1].rotate(rot)

        # 지금 돌릴애랑 숫자 1, 3 차이나고, 플래그 있으면 반대로 돌기
        for jdx in range(4):
            if flag[jdx]:            
                diff = abs(idx - jdx)
                if diff == 1 or diff == 3:
                    magnets[jdx - 1].rotate(-rot)
                # 지금 돌릴애랑 숫자 2 차이나고, 플래그 있으면 같은 방향으로 돌리기
                else:
                    magnets[jdx - 1].rotate(rot)

    ans = sum([mag[0] for mag in magnets])
    return ans


T = int(input())
for tc in range(1, T + 1):
    k = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    cmds = [list(map(int, input().split())) for _ in range(k)]
    ans = solve(k, magnets, cmds)

    # print(magnets)
    # print(cmds)
    print(f"#{tc} {ans}")