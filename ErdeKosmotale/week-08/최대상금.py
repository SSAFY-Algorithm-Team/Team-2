# 중복순열인가.... 언제든 뭐랑 바꿔도 상관없으니까

def dfs(idx):

    global ans_num

    # if(num_str == optimized_str):
    #     #print(optimized_str)
    #     ans_num = int(''.join(optimized_str))
    #     return 

    if(idx == n_ex):

        ans_num = max(ans_num,int(''.join(num_str)))
        return

    if(str(num_str) in visited):
        return

    visited.add(str(num_str))

    for i in range(len(num_str)):
        for j in range(len(num_str)):
            if(i==j):continue
            num_str[i], num_str[j] = num_str[j], num_str[i]
            dfs(idx+1)
            num_str[j], num_str[i] = num_str[i], num_str[j]

T = int(input())

for test_case in range(1,T+1):

    num_str, n_ex = input().split()
    ans_num = 0 

    n_ex = int(n_ex)
    num_str = list(num_str)

    optimized_str = sorted(num_str, reverse = True)

    visited=set()

    dfs(0)

    print(f"#{test_case} {ans_num}")






# 버블소트를 중간까지 실시하면 될 것 같은 걸

################################################################

# 버블 소트 흡사하게는 풀 수 없을 것 같습니다.

# T = int(input())

# for test_case in range(1,T+1):

#     num_str, n_ex = input().split()
#     ans_num = 0 

#     n_ex = int(n_ex)
#     num_str = list(num_str)

#     # 최대일 때를 찾아야 하니까 !!

#     num_idx = len(num_str)

#     max_idx = 0
#     max_val = 0

#     if(n_ex >= num_idx):
#         n_ex = num_idx-1

#     for i in range(n_ex):
#         max_idx = i
#         max_val = int(num_str[i])

#         for j in range(i,num_idx):

#             if(int(num_str[j]) > max_val):
#                 max_idx = j
#                 max_val = int(num_str[j])
        
#         num_str[i], num_str[j] = num_str[j] , num_str[i]

#     ans = ''.join(num_str)

# print(f"#{test_case} {ans}")
        

# def combination():

#     path = []
#     result = []
#     def backtrack(start):

#         if(len(path)==2):
#             result.append(path[:])
#             return

#         for i in range(start,len(num_str)):

#             path.append(i)
#             backtrack(i+1)
#             path.pop()

#     backtrack(0)

#     return result    

        
        