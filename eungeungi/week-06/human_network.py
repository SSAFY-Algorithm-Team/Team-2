# 본인이 가지고 있는 값들 +1
# 남은 값 중에서 자기 자신을 value로 갖고 있는 값 찾기
# 그것조차 없다면 본인이 가지고 있는 값을 value로 갖고 있는지 찾기

# flatten으로 되어있으니 n단위로 끊어서 보긴할건데
# i가 n단위 j 는 i보다 큰 경우만 파악
# 즉 N의 경우는 i를 1부터 N-1까지 탐색하는데 j는 i+1탐색  

# x 0 1 0 0
# 1 x 1 1 0
# x x x 0 1
# x x x x 0
# x x x x x
# -----------------
# x 0 1 1 0
# x x 1 0 0
# 1 1 x 0 1
# x x x x 0
# x x x x x

# 1 [3,4]
# 2 [3]  
# 3 [1,2,5]
# 4 [1,5]
# 5 [3,4]

def net(N,ls):



T = int(input())
for tc in range(1,T+1):
    ls = list(map(int,input().split()))
    N = ls[0]
    ls = ls[1:]
    arr = []
    new = [[]]
    for i in range(N-1):
        for j in range(i+1,N):
            new[i].append(arr[i][j])
    ans = net(N,ls)