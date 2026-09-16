T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    result = 0
    # 먼저 D,W가 적기 때문에
    # 일단 ㅠㅠ 안되는 곳 찾기 
    # 
    # D = 세로, W = 가로, K = 합격기준  
    D,W,K = map(int,input().split())
    arr = []
    for i in range(D):
        arr.append(list(map(int,input().split())))
    def check(arr):
        

    print(f"#{test_case} {result}")