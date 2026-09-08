T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 초기 접근
    # 일단 사칙연산 배열 만들기
    # dfs로
    N = int(input())
    arr_cal = list(map(int, input().split()))   # ['+','-','*','/'] 개수 (map -> list로 변환!)
    arr_num = list(map(int, input().split()))   # 게임판 숫자들
 
    max_val = -float('inf')
    min_val = float('inf')
 
    def cal(a, b, n):
        if n == 0:
            return a + b
        elif n == 1:
            return a - b
        elif n == 2:
            return a * b
        elif n == 3:
            # 나눗셈은 소수점 이하 버림(0 방향 truncation)
            if a * b < 0 and a % b != 0:
                return a // b + 1
            else:
                return a // b
        else:
            print("수식입력 틀림")
 
    def dfs(a, count):
        # a     : 여기까지 계산된 값
        # count : 지금까지 사용한 숫자 개수 (다음에 쓸 숫자는 arr_num[count])
        global max_val, min_val
 
        if count == N:
           # print("###############한줄 완료", a) 
            max_val = max(max_val, a)
            min_val = min(min_val, a)
            return
 
        for n in range(4):
            if arr_cal[n] > 0:
                arr_cal[n] -= 1
                b = arr_num[count]
                dfs(cal(a, b, n), count + 1)
                arr_cal[n] += 1  # 백트래킹: 카드 원복
 
    dfs(arr_num[0], 1)
 
    result = max_val - min_val
    print(f"#{test_case} {result}")