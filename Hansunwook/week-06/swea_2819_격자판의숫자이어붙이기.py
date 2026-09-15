T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = [0]
    arr = []
    visit = []
    arr_in = []
    for i in range(4):
        arr.append(list(map(int,input().split())))
        visit.append([False]*4)
        arr_in.append([0]*4)
    
    numbers = set()
    udrl = [[0,1],[0,-1],[1,0],[-1,0]]
    def dfs(i,j,count,num):
        if count == 7:
            numbers.add(num)
            return
        for k in range(4):
            a = i 
            b = j
            a += udrl[k][0]
            b += udrl[k][1]
            if 0<=a<4 and 0<=b<4:
                num = num*10 + arr[a][b]
                dfs(a,b,count+1,num)
                visit[a][b] = False
                num = num//10
    for i in range(4):
        for j in range(4):
            dfs(i,j,1,arr[i][j])
    result = len(numbers)
    print(f"#{test_case} {result}")
