T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = [0]
    number, change = map(int,input().split())
    numbers = list(map(int, number))
    #뒤집어서 제일 큰수 만들기
    #
    print(f"{test_case} {result[0]}")