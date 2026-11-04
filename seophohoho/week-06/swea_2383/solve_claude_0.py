def solve(N, grid):
    people = []
    stairs = []  # [(r, c, K), (r, c, K)]  -> stairs[0]=stair_a, stairs[1]=stair_b
    for r in range(N):
        for c in range(N):
            v = grid[r][c]
            if v == 1:
                people.append((r, c))
            elif v >= 2:
                stairs.append((r, c, v))

    def dist(p, s):
        return abs(p[0] - s[0]) + abs(p[1] - s[1])

    def simulate_wave(ready_times, K):
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

    s0_pos, s0_len = stairs[0][:2], stairs[0][2]
    s1_pos, s1_len = stairs[1][:2], stairs[1][2]

    # 각 사람마다 "이동 시간이 더 적게 걸리는 계단"으로 바로 배정
    ready_a, ready_b = [], []
    for p in people:
        da = dist(p, s0_pos)
        db = dist(p, s1_pos)
        if da <= db:
            ready_a.append(da + 1)
        else:
            ready_b.append(db + 1)

    finish_a = simulate_wave(ready_a, s0_len)
    finish_b = simulate_wave(ready_b, s1_len)

    return max(finish_a, finish_b)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(N, grid)}")