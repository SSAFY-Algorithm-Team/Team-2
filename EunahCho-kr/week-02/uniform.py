# programmers 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 소요시간 : 25분 / 시도 : 2회

def solution(n, lost, reserve):
    uniforms = [1] * (n + 2) # 앞 뒤 패딩값 -> 탐색시 인덱스 에러 방지
    for r in reserve:
        uniforms[r] += 1

    for l in lost:
        uniforms[l] -= 1


    for i in range(1, n+1):
        if uniforms[i] == 0:
            if uniforms[i-1] == 2: # 왼쪽 먼저 탐색
                uniforms[i-1] = 1
                uniforms[i] = 1
            elif uniforms[i+1] == 2: # 안되면 오른쪽
                uniforms[i+1] = 1
                uniforms[i] = 1

    answer = 0
    for uniform in uniforms[1:-1]: # 패딩값 빼고, 값이 있는 개수 세기
        if uniform:
            answer += 1

    return answer
