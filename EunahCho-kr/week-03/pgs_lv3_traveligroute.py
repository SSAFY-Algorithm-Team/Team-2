# 프로그래머스 Lv3. 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 시간  3h / 시도 10

def solution(tickets):
    tickets.sort(key = lambda x: x[1])
    # print("ticekets", tickets)
    n = len(tickets)
    is_used = [False] * n
    flag = False
    answer = []

    def dfs(depth):
        nonlocal answer, flag
        # print(depth," / ",path)
        if depth == n - 1:
            answer = path[:]
            flag = True # 깊이의 가장 끝까지 간 경우 true
            return answer
        
        for i in range(n):
            if not is_used[i] and tickets[i][0] == path[-1]:
                is_used[i] = True
                path.append(tickets[i][1])
                dfs(depth + 1)
                
                if flag: # 길이에 맞는 첫 번째 애가 정답임 => 함수가 지정 길이에 도달했으면 break
                    break
                    
                is_used[i] = False
                path.pop()

    for i in range(n): # 인천 출발
        # print("인천 있는 티켓 탐색 : ", i)
        path = ["ICN"] # 변수 초기화
        if tickets[i][0] == "ICN":
            path.append(tickets[i][1])
            is_used[i] = True
            dfs(0)
            is_used[i] = False # dfs 끝나면 원래대로 돌려주기
            if flag: # dfs 끝까지 돌렸을 때(= 길이가 n + 1일 때)만 출력 -> 아니면 다음 반복문
                return answer