# 직원들 번호 1-N, 할 일 번호 1-N
# 순열인 것 같은데

def permutation():

    used = [False] * (N)
    answer = 0

    def backtrack(prob,K):

        nonlocal answer

        if(prob <= answer):
            return

        
        if K == N :

            if(prob >= answer):
                answer = prob
            return

        for i in range(N):

            if(not used[i]):
            
                used[i] = True
                now_prob = lst[K][i]/100
                backtrack(prob*now_prob,K+1)
                used[i] = False
                    
    backtrack(1,0)
    
    return answer

T = int(input())

for test_case in range(1,T+1):

    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]

    # lst_people = list(i for i in range(1 , N + 1))

    ans = permutation()

    ans = f"{100 * ans:.6f}" 

    print(f"#{test_case} {ans}")