import sys
from itertools import combinations

## dfs안써도 된다


def get_best_profits(honeys, n, m, c):
    """
    모든 (row, start_col) 가로 M칸 구간에 대해
    합이 C 이하인 부분집합 중 최대 수익(제곱합)을 계산.
    반환: segments = [(row, start_col, best_profit), ...]
    """
    segments = []
    for x in range(n):
        for y in range(n - m + 1):
            arr = honeys[x][y:y + m]
            best = 0
            # 부분집합 완전탐색 (최대 2^5 = 32가지, M <= 5라 매우 빠름)
            for k in range(1, m + 1):
                for comb in combinations(arr, k):
                    s = sum(comb)
                    if s <= c:
                        profit = sum(v * v for v in comb)
                        if profit > best:
                            best = profit
            segments.append((x, y, best))
    return segments


def solve(n, m, c, honeys):
    segments = get_best_profits(honeys, n, m, c)

    # 행(row)별로 구간들을 묶어두면 "다른 행"인 경우 겹침 체크 없이 바로 더할 수 있음
    by_row = {}
    for x, y, p in segments:
        by_row.setdefault(x, []).append((y, p))

    rows = sorted(by_row.keys())
    row_best = {x: max(p for _, p in by_row[x]) for x in rows}  # 각 행의 전체 최댓값

    ans = 0

    # Case 1: 서로 다른 두 행에서 각각 하나씩 고르는 경우
    #   -> 겹칠 일이 없으므로 각 행의 최댓값끼리만 비교하면 됨
    if len(rows) >= 2:
        # 상위 두 행의 최댓값만 있으면 충분
        top_vals = sorted(row_best.values(), reverse=True)
        ans = max(ans, top_vals[0] + top_vals[1])

    # Case 2: 같은 행 안에서 겹치지 않는 두 구간을 고르는 경우
    for x in rows:
        segs = by_row[x]
        segs_n = len(segs)
        for i in range(segs_n):
            y1, p1 = segs[i]
            for j in range(i + 1, segs_n):
                y2, p2 = segs[j]
                if y1 + m <= y2 or y2 + m <= y1:  # 겹치지 않음
                    ans = max(ans, p1 + p2)

    return ans


def main():
    sys.stdin = open('input.txt', 'r')
    T = int(input())
    results = []
    for tc in range(1, T + 1):
        N, M, C = map(int, input().split())
        honeys = [list(map(int, input().split())) for _ in range(N)]
        ans = solve(N, M, C, honeys)
        results.append(f"#{tc} {ans}")
    print("\n".join(results))


if __name__ == "__main__":
    main()