def solution(tickets):
    answer = []
    # 초기 접근
    # 끝까지 가야하기 때문에 깊이우선
    # 하나 잡고 겹치면 알파벳먼저 끊기면 다른거
    #하나 끝나면 끝
    
    # 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
    # 문제 잘읽기...................
    # ㅠㅠ
    # 항상 "ICN" 공항에서 출발..
    
    len_arr =len(tickets)
    visit = [False]*len_arr
    post = []
    #알파벳 순서로 하는건 어떻게 하지? 넣기 전??
    def dfs():
        nonlocal answer
        if len(post) == len_arr+1:
            # print("---------------------------------------")
            # print("##########항공표 만들기 성공")
            # print("항공표: ",post)
            # print("---------------------------------------")
            if len(answer) == 0:
                answer = post[:]
            elif post < answer:
                # print("바꿈")
                answer = post[:]
            return 
        for i in range(len_arr):
            # print("항공표 보는중........",i)
            # print(tickets[i])
            # print("현재 post:",post)
            if visit[i]:
                continue
            #처음에 없으면 그냥 집어넣음
            if len(post) == 0 :
                if tickets[i][0] != "ICN":
                    continue
                visit[i] = True
                post.append(tickets[i][0])
                post.append(tickets[i][1])
                dfs()
                post.pop()
                post.pop()
                visit[i] = False
                continue
            # post 끝이랑 지금 보는 여행표랑 비교
            #만약에 연결 가능하면 post에 넣은 후에 그 다음으로 넘어가기
            # print(post[-1],tickets[i],"비교중..")
            if post[-1] == tickets[i][0]:
                # print("!!!!!!연결 성공: ",post[-1], tickets[i])
                post.append(tickets[i][1])
                visit[i] = True
                dfs()
                post.pop()
                visit[i] = False
    dfs()
    return answer