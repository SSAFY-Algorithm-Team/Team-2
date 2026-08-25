# SWEA 5215. 햄버거 다이어트 (D3)
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# 소요시간 2h 30m/ 시도 : 3


def solve(n, l, info):
    dp = [[0] * (l + 1) for _ in range(n + 1)] # dp[i][j] = i개까지 재료에서 j칼로리 이내 최고 맛 점수 

    info.sort(key=lambda x:x[1]) # 두 번째 원소로 정렬하기
    info = [(0,0)] + info

    for i in range(1, n + 1):
        scr, cal = info[i]
        for j in range(1, l + 1):
            if cal <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cal] + scr)
            else:
                dp[i][j] = dp[i-1][j]

    return max(dp[n])


def main():
    T = int(input())
    for t in range(1, T+1):
        n, l = map(int, input().split())
        info = [tuple(map(int, input().split())) for _ in range(n)]
        ans = solve(n, l, info)
        print(f"#{t} {ans}")


if __name__ == "__main__":
    main()



# 첫 시도 였던거...
# dp = [[0] * (n + 1) for _ in range(n + 1)]
# dp[0][?] = 제한 칼로리 안넘는 맛 점수
# dp[1][?] = 제한 칼로리 안넘으면 맛 점수 추가

    # for i in range(n): # 재료 한 개인 거 -> 초기값
    #     if info[i][1] <= l:
    #         dp[0][i] = info[i][0]
    # print(dp)

    # for c in range(n):
    #     tmp_cal = dp[0][c]
    #     for r in range(1, n):
    #         if tmp_cal + info[r][1] <= l:
    #             tmp_cal += info[r][1]
    #             dp[r][c] = dp[r - 1][c] + info[r][0]
    #         else:
    #             dp[r][c] = dp[r - 1][c]
    # print(dp)


# 두번째
# dp[i][j] = i개까지 재료에서 j칼로리 이내 최고 맛 점수 
# 칼로리 정보를 열에 넣음
    # -> 현재 재료가 들어갈 수 있다면 (칼로리가 제한 이내), max(dp[i-1][j], dp[i-1][j-cal] + scr)
                                                    # 이전 재료까지만 넣기 vs 지금 재료 넣기
    # -> 아니면, 걍 이전 재료까지만