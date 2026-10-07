from collections import deque

def find(R, C, arr):
    # 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # visited[x][y][direction][memory]
    visited = [[[[False] * 16 for _ in range(4)]
                for _ in range(C)]
               for _ in range(R)]

    queue = deque()
    queue.append((0, 0, 0, 0))

    while queue:
        x, y, direction, memory = queue.popleft()

        # 이미 완전히 같은 상태를 방문했으면 넘어감
        if visited[x][y][direction][memory]:
            continue

        visited[x][y][direction][memory] = True

        cmd = arr[x][y]

        # 종료 명령
        if cmd == '@':
            return "YES"

        # 방향 변경
        if cmd == '>':
            direction = 0

        elif cmd == 'v':
            direction = 1

        elif cmd == '<':
            direction = 2

        elif cmd == '^':
            direction = 3

        # 메모리에 따라 방향 변경
        elif cmd == '_':
            if memory == 0:
                direction = 0
            else:
                direction = 2

        elif cmd == '|':
            if memory == 0:
                direction = 1
            else:
                direction = 3

        # 메모리 변경
        elif cmd.isdigit():
            memory = int(cmd)

        elif cmd == '+':
            memory = (memory + 1) % 16

        elif cmd == '-':
            memory = (memory - 1) % 16

        # ?는 네 방향 모두 가능
        if cmd == '?':
            for nd in range(4):
                nx = (x + dx[nd]) % R
                ny = (y + dy[nd]) % C

                if not visited[nx][ny][nd][memory]:
                    queue.append((nx, ny, nd, memory))

        # 일반 명령은 현재 방향으로 한 칸 이동
        else:
            nx = (x + dx[direction]) % R
            ny = (y + dy[direction]) % C

            if not visited[nx][ny][direction][memory]:
                queue.append((nx, ny, direction, memory))

    return "NO"


T = int(input())

for tc in range(1, T + 1):
    R, C = map(int, input().split())

    arr = []

    for _ in range(R):
        row = list(input().strip())
        arr.append(row)

    ans = find(R, C, arr)

    print(f"#{tc} {ans}")