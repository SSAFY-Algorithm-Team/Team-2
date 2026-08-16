# 프로그래머스, 정수삼각형
# 풀이시간: 5분 이내


def solution(triangle):
    
    #그거인 것 같네 그거... 다이나믹 프로그래밍
    
    depth=len(triangle)
    
    for i in range(depth-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j]+= max(triangle[i+1][j],triangle[i+1][j+1])
            
    answer=triangle[0][0]
    
    
    
    return answer