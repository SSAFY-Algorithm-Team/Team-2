# 프로그래머스 Lv2. 2xn 타일링
# https://school.programmers.co.kr/learn/courses/30/lessons/12900?language=python3
# 소요시간 20분 / 시도 2회

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        _, dp[i] = divmod(dp[i-1] + dp[i-2], 1000000007)
        # print(dp)
    answer = dp[n]
    return answer


"""
제한사항
    가로의 길이 n은 60,000이하의 자연수 입니다.
    경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

첫 시도 : _, answer = divmod(dp[n], 1000000007)
=> 마지막에 한 번만 나눔
    => 파이썬은 큰 정수 덧셈이 자릿수에 비례해서 느려지기 때문에, 
    뒤로 갈수록 덧셈 한 번 한 번이 점점 느려지면서 전체적으로 O(n²)에 가까운 시간이 걸림

해결 :  _, dp[i] = divmod(dp[i-1] + dp[i-2], 1000000007)
=> for 문 안에서 계속 나눔
    => 나눗셈은 짜피 O(1)
    """