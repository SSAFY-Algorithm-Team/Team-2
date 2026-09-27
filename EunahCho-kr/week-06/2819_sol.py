import sys

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def solve(board):
    ans_list = set()
    path = []

    def dfs(x, y, depth):
        if depth == 7:
            ans_list.add(''.join(map(str, path)))
            return

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                path.append(board[nx][ny])
                dfs(nx, ny, depth + 1)
                path.pop()

    for x in range(4):
        for y in range(4):
            dfs(x, y, 0)
    # print(ans_list)
    return len(ans_list)


def main():
    sys.stdin = open('2819_input.txt', 'r')
    t = int(input())
    for tc in range(1, t+1):
        board = [list(map(int, input().split())) for _ in range(4)]
        ans = solve(board)
        print(f"#{tc} {ans}")


if __name__ == '__main__':
    main()