# 중복순열인가.... 언제든 뭐랑 바꿔도 상관없으니까


def combination():

    path = []
    result = []
    def backtrack(start):

        if(len(path)==2):
            result.append(path[:])
            return

        for i in range(len(num_str)):

            path.append(i)
            backtrack(i+1)
            path.pop()

    backtrack(0)

    return result



T = int(input())

for test_case in range(1,T+1):

    num_str, n_ex = map(str,input().split())

    ans_num = 0 # 최대일 때를 찾아야 하니까 !!

    idx = len(num_str) - 1

    print(combination())