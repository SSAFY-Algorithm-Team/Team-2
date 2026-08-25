#SWEA 햄버거 다이어트

# 0/1 배낭 문제와 완전히 동일

# 완전탐색으로도 풀 수 있어야 합니다.

T=int(input())

for test_case in range(1,T+1):

    N, LIMIT=map(int,input().split())
    items=[]
    for _ in range(N):
        items.append(list(map(int,input().split())))

    dp = [0] * (LIMIT + 1)
    for score, kcal in items:
        for c in range(LIMIT, kcal - 1, -1):
            dp[c] = max(dp[c], dp[c - kcal] + score)
    best = dp[LIMIT]
    print(dp)
    print(f"#{test_case} {best}")



# def combinations(kcals,scores,r,limit):

#     path=[]
#     path_score=[]
#     result_score=[]

#     n=len(kcals)

#     def backtrack(start):

        
#         sum_path=0
#         for i in range(len(path)):
#             sum_path+=path[i]
#             if(sum_path>limit):
#                 return
        
#         if(len(path)==r):
            
#             result_score.append(sum(path_score))
#             return

#         for i in range(start,n):
            
#             path.append(kcals[i])
#             path_score.append(scores[i])
#             backtrack(i+1)
#             path.pop()
#             path_score.pop()

#     backtrack(0)

#     return result_score

# T=int(input())

# for test_case in range(1,T+1):

#     N, LIMIT=map(int,input().split()) #햄버거 수, 제한 칼로리

#     scores=[]
#     kcals=[]
#     for i in range(N):
#         score,kcal=map(int,input().split())

#         scores.append(score)
#         kcals.append(kcal)

#     result_ans=0

#     for i in range(1,N+1):
#         result=combinations(kcals,scores,i,LIMIT)

#         if(not result):
#             continue
#         result_ans=max(result_ans,max(result))

#     print(f"#{test_case} {result_ans}")    
        


T=int(input())

for test_case in range(1,T+1):

    N, LIMIT=map(int,input().split())
    items=[]
    for _ in range(N):
        items.append(list(map(int,input().split())))

    dp = [0] * (LIMIT + 1)
    for score, kcal in items:
        for c in range(LIMIT, kcal - 1, -1):
            dp[c] = max(dp[c], dp[c - kcal] + score)
    best = dp[LIMIT]
    print(dp)
    print(f"#{test_case} {best}")