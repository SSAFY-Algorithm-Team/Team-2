# # programmers 타겟 넘버
# # https://school.programmers.co.kr/learn/courses/30/lessons/43165
# # 소요 시간 : 2h 10m / 시도 횟수 : ?

def solution(numbers, tartget):
    arr = [-1, 1]
    m = len(numbers)
    path = []
    answer = 0
    def dfs(depth):
        nonlocal answer
        if depth == m:
            # print(path)
            tmp = 0
            for i in range(m):
                tmp += path[i] * numbers[i]
            if tmp == tartget:
                answer += 1
            return
        
        for i in range(len(arr)):
            path.append(arr[i])
            dfs(depth+1)
            path.pop()
        return answer

    dfs(0)
    return answer

# print(solution([4, 1, 2, 1], 4))

"""
1. -1, 1로 numbers와 같은 길이의 중복순열 만듦
2. numbers의 각 자리 수와 곱함
3. target과 일치 시 answer += 1
"""
