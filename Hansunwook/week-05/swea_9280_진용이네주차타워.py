T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    n,m = map(int,input().split())
    Ri = []
    Wi = []
    X = []
    for i in range(n):
        Ri.append(int(input()))
    for i in range(m):
            Wi.append(int(input()))
    for i in range(m*2):
            X.append(int(input()))
    # print(Ri,Wi,X)
    
    print(f"#{test_case} {result}")