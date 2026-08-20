def solution(n):
    # 처음엔 재귀로 풀었다가 런타임 에러 떠서 그냥 for 문으로 바꿨다..
    # 그냥 두번째 값을 첫번째 값으로, 둘이 더한 값은 두번째 값으로 설정
    answer = 0
    a = 0
    b = 1
    for i in range(n-1):
        fibo = a+b
        a = b
        b = fibo
    k = 1234567
    answer = fibo % k
    return answer