
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    input()
    arr = []
    for i in range(100):
        arr.append(list(map(int,input().split())))
    def run1():
        for i in range(100):
            if arr[99][i] == 2:
                return check(i)
    def check(i):
        a = 99
        b = i
        before = 0
        while(1):
            if a == 0:
                return b
            if before != 1 and b+1 < 100 and arr[a][b+1] ==1:
                b += 1
                before = 2
            elif before != 2 and b-1 >= 0 and arr[a][b-1] ==1:
                b -= 1
                before = 1
            elif a > 0:
                a -= 1
                before = 0

    result = run1()

    print(f"#{test_case} {result}")