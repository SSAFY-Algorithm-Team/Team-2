T = int(input())
for test_case in range(1, T + 1):
    # 일단 각자의 맨홀뚜껑에 따라 갈 수 있는 방향에 대해 정의하고
    # 시간이 흐를 때마다 넓게 전부 가는? 그런식으로 해야하나
    # 그럼 bfs? 
    # 배열에 넣어서 마지막 끝나면 그 개수 세면 되지 않을까..


    # 근데 이 맨홀뚜껑이 갈 수 있는 곳 그냥 내가 다 정의해야하는건가
    #그렇다면
    # 하상우좌
    #[1,-1,0,0]
    #[0,0,1,-1]
    # 1->0,1,2,3
    # 2->0,1
    # 3->2,3
    # 4->1,2
    # 5->0,2
    # 6->0,3
    # 7->1,3

    ud = [1,-1,0,0]
    rl = [0,0,1,-1]
    #-> 너무 많으니까 그냥 2차원 배열 만들기
    t = [[-1],[0,1,2,3],[0,1],[2,3],[1,2],[0,2],[0,3],[1,3]]

    #N,M 배열 R,C 위치 L 시간
    N,M,R,C,L = map(int,input().split())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    # print(arr)
    #맨홀 연결됐는지도 확인해야함 어떻게?
    #-> 그쪽으로 간 숫자에 대응되는 숫자 있을 경우-> 0,1   2,3 이렇게 묶음임
    # 잘 모르겠음 그냥 일단 조건문으로 처리
    # 0 1   1 0   2 3   3 2
    pair = [1,0,3,2]
    answer = 1
    arr_list = [[R,C]]

    visit = [[True] * M for _ in range(N)]
    visit[R][C] = False
    for i in range(L-1):
        # print("##############1시간 지남################, 시간: ",i)

        # # 근데 넓어질수록 더 커져서 음....
        # # 끝부분? 어딘지 저장하는 배열이나 그런게 있으면 가능할듯..
        arr_len = len(arr_list)
        # print("겉에 위치한 터널",arr_list)
        # print("겉에 위치한 터널 개수",arr_len)
        for i in range(arr_len):
            # 하나씩 꺼내서 앞에서 pop 한 후 뒤에서부터 append
            # 문제는 이렇게 할 경우 len이 달라져서 저장 한 후?? 해결 일단 나중에
            R,C = arr_list.pop(0)
            # print("=================이 위치 배열에서 맨홀 이동중.. ",R,C)
            for i in t[arr[R][C]]:
                # print(arr[R][C],"터널 구조물 타입 발견...........")
                # print(i,"방향으로 맨홀 이동중........")
                R_u = R + ud[i]
                C_u = C + rl[i]
                #맨홀 연결됐는지 확인 후 가능할 경우 answer +1 
                #그리고 들어간 맨홀 어딘지 저장 후 거기 방문
                #!!!!추가적으로 이미 방문했으면 건너뛰기
                if 0<=R_u<N and 0<=C_u<M:
                    if pair[i] in t[arr[R_u][C_u]] and visit[R_u][C_u]:
                        # print("연결 가능, 맨홀 저장 완료")
                        answer += 1
                        arr_list.append([R_u,C_u])
                        visit[R_u][C_u] = False
                        # print("배열에 추가 완료",arr_list)
                        # print("이만큼 갈 수 있음",answer)
                    # else:
                    #     # print("연결 불가능")
    print(f"#{test_case} {answer}")