# 4013. [모의 SW 역량테스트] 특이한 자석
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH&categoryId=AWIeV9sKkcoDFAVH&categoryType=CODE&problemTitle=4013&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 1h 30m / 시도 2

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


def solve(magnets, cmds):

    # cmds를 돌면서
    for idx, rot in cmds:
        idx -= 1 # 0-based

        # 돌리기 전에 현재 마그넷의 2, 6 인덱스들 확인 (1번자석의 6, 4번 자석의 2는 제외)
        flag = [False] * 3
        for i in range(3):
            # 극이 다르다면 -> 같이 돌 애 -> 플래그
            if magnets[i][2] != magnets[i + 1][6]:
                flag[i] = True
 
        magnets[idx].rotate(rot)

        tmp_i = idx - 1 # 자신보다 왼쪽 확인
        tmp_rot = -rot
        while tmp_i >= 0 and flag[tmp_i]:
            magnets[tmp_i].rotate(tmp_rot)
            tmp_i -= 1
            tmp_rot *= -1

        tmp_i = idx + 1 # 자신보다 오른쪽 확인
        tmp_rot = -rot
        while tmp_i < 4 and flag[tmp_i - 1]:
            magnets[tmp_i].rotate(tmp_rot)
            tmp_i += 1
            tmp_rot *= -1        

    ans = 0
    for idx, mag in enumerate(magnets):
        if mag[0]:
            ans += 2 ** idx

    return ans


T = int(input())
for tc in range(1, T + 1):
    k = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    cmds = [list(map(int, input().split())) for _ in range(k)]
    ans = solve(magnets, cmds)

    print(f"#{tc} {ans}")



## 오른쪽 왼쪽 한번에 시도했던거 => 누구의 플래그인지 확실하지 않아서 실패 
# (이때는 플래그 길이 4로 각 자석에 대한 플래그였음 - 지금은 이음새에 대한 플래그)

# # 지금 돌릴애랑 숫자 1, 3 차이나고, 플래그 있으면 반대로 돌기
# for jdx in range(1, 5):
#     if flag[jdx]:            
#         diff = abs(idx - jdx)
#         if diff == 1 or diff == 3:
#             magnets[jdx - 1].rotate(-rot)
#         # 지금 돌릴애랑 숫자 2 차이나고, 플래그 있으면 같은 방향으로 돌리기
#         else:
#             magnets[jdx - 1].rotate(rot)