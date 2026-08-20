# programmers 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 시간 : 40m / 횟수 : 2

def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[1][0] + triangle[0][0]
    dp[1][1] = triangle[1][1] + triangle[0][0]
    # print(dp[0][0], dp[1][0], dp[1][1])

    for i in range(2, n):
        m = len(triangle[i])
        for j in range(m):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == m - 1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    # print(dp)

    answer = max(dp[n-1])
    # print(answer)
    return answer

# if __name__ == "__main__":
#     solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])