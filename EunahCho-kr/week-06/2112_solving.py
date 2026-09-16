"""
투명한 막 (bar 모양의 셀 가르방향으로 W개) D장 쌓음 => 두께 D (3-13), 넓이 W (1-20)
성능 평가를 위한 합격기준 K -> 세로 방향으로 동일한 특성의 셀이 k(1-D)개 이상 연속

약품 막 별로 투입 -> 투입하는 막의 모든 셀은 하나의 특성으로 변경됨

약물 투입 횟수는 최소 2 => 최종 약물 투입 횟수의 최소값 출력 / 투입하지 않고 성능검사 통과 가능하면 0 출력

T
D W K
1번 막
2번 막
...
"""
import sys
from itertools import combinations


def check(d, w, k, cells, checked_n):  # 현재 상태 확인 후, 통과 가능한지 아닌지 return

    for wi in range(w):
        max_cnt = curr_cnt = 1
        prev = -1
        for di in range(d):
            if prev == cells[di][wi]:
                curr_cnt += 1
            else:
                curr_cnt = 1
            prev = cells[di][wi]
            max_cnt = max(max_cnt, curr_cnt)
        checked_n[wi] = max_cnt

    for cnt in checked_n:
        if cnt < k:
            return False

    return True


def solve(d, w, k, cells):
    """
    check : 넓이 W와 같은 리스트 생성 -> 각 연속되는 특성 수 셀 거
    -> 이때 안의 원소가 다 k 보다 크면 0 출력

    약물 한 줄씩 넣어보기 -> for di in d: -> 돌때마다 "check 업데이트" -> 함수로 따로 빼기 + 약물 += 1
    -> 되면 0 출력

    약물 두 줄 씩 -> for di1, di2 in combination(d, 2): -> check 업데이트 + 약물 += 1
    -> 이제 약물 수 출력
    """
    checked_n = [0] * w
    is_poss = check(d, w, k, cells, checked_n) # 현재 강도 확인 및 checkd_n에 넣음 + 되면 return

    if is_poss:
        return 0

    for ans in range(1, d + 1):
        for comb in combinations(range(d), ans):
            cells_tmp = [row[:] for row in cells]
            for com in comb:
                for i in range(2):
                    cells_tmp[com] = [i] * w  # A로 다 바꿔보고 check, 되면 return
                    is_poss = check(d, w, k, cells_tmp, checked_n)

                if is_poss:
                    # print(comb)
                    # for row in cells_tmp:
                    #     print
                    #     (row)
                    if ans < 2:
                        return 0
                    else:
                        return ans


def main():
    sys.stdin = open('2112_input.txt', 'r')
    t = int(input().rstrip())
    for tc in range(1, t + 1):
        d, w, k = map(int, input().split())
        cells = [list(map(int, input().split())) for _ in range(d)]
        if tc == 1:
            ans = solve(d, w, k, cells)
            print(f"#{tc} {ans}")


if __name__ == '__main__':
    main()