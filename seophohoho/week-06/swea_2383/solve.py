T = int(input())

def get_dist(person,stair):
    return abs(person[0]-stair[0]) + abs(person[1]-stair[1])

def run_wave(ready_times, K):
    if not ready_times:
        return 0

    waiting = sorted(ready_times)
    n = len(waiting)
    idx = 0
    slots = [None, None, None]
    finished = 0
    last_finish = 0
    wave = 0

    while finished < n:
        # (1) 슬롯 정리 — 이번 wave에 완료되는 사람 빠져나감
        for i in range(3):
            if slots[i] is not None and slots[i] == wave:
                slots[i] = None
                finished += 1
                last_finish = max(last_finish, wave)

        # (2) 빈 슬롯에 대기 중인 사람 입장
        for i in range(3):
            if slots[i] is None and idx < n and waiting[idx] <= wave:
                slots[i] = wave + K
                idx += 1

        wave += 1

    return last_finish

for tc in range(1,T+1):
    N = int(input())

    room = [list(map(int,input().split())) for _ in range(N)]
    people = []
    stairs = []

    # 방 Full scan(사람과 계단을 찾기)
    for i in range(N):
        for j in range(N):
            target = room[i][j] 
            if target == 1:
                people.append((i,j))
            elif target >= 2:
                stairs.append((i,j,target))

    # 계단 정보 뺴오기
    stair_a_pos = stairs[0][:2]
    stair_a_len = stairs[0][2]

    stair_b_pos = stairs[1][:2]
    stair_b_len = stairs[1][2]

    # 각 사람을 어느 계단에 배정할까??에 대한 것
    ready_stair_a = []
    ready_stair_b = []

    for person in people:
        dist_a = get_dist(person, stair_a_pos)
        dist_b = get_dist(person, stair_b_pos)

        if dist_a <= dist_b:
            ready_stair_a.append(dist_a+1)
        else:
            ready_stair_b.append(dist_b+1)

    # Wave 돌리기 ㄱㄱㄱ
    result_stair_a = run_wave(ready_stair_a,stair_a_len)
    result_stair_b = run_wave(ready_stair_b,stair_b_len)

    answer = max(result_stair_a, result_stair_b)

    print(f"#{tc} {answer}")