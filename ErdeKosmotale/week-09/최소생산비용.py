
#퍼뮤테이션을 구하면 될듯 n개만 고르면 되니까 !!

def permutation():

    global ans
    used = [0] * n

    def backtrack(idx,now_cost):
        global ans

        if(now_cost>=ans):
            return

        if(idx==n):
            ans = now_cost

        for i in range(n):

            if(not used[i]):

                used[i] = True
                plus_cost= lst[idx][i]
                backtrack(idx+1,now_cost + plus_cost )
                used[i] = False

    backtrack(0,0)


T = int(input())

for test_case in range(1, T + 1):

    n = int(input())

    lst = [list(map(int,input().split())) for _ in range(n)]

    ans= 10**9

    permutation()

    print(f"#{test_case} {ans}")