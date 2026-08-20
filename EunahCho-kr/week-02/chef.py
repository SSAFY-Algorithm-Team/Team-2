# SWEA D4 DFS 부분집합 요리사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&
# 소요시간 : 1h / 시도 : 2


def calculate(path, board):
    ans = 0
    n = len(path)
    for i in range(n):
        for j in range(i + 1, n):
            x = path[i]
            y = path[j]
            ans += board[x][y]
            ans += board[y][x]
    return ans


def solve(n, board):
    path = []
    is_used = [False] * n
    min_ans = float('inf')

    def dfs(depth, prev_i):
        nonlocal min_ans
        # print("depth ", depth)
        # print("path ", path)

        if depth == n // 2:
            rest_path = [i for i in range(n) if i not in path]
            # print("rest path ", rest_path)
            ans = abs(calculate(path, board) - calculate(rest_path, board))
            min_ans = min(min_ans, ans)
            return

        for i in range(prev_i, n):
            if not is_used[i]:
                path.append(i)
                is_used[i] = True
                prev_i = i
                dfs(depth+1, prev_i)
                path.pop()
                is_used[i] = False

    dfs(0, 0)
    return min_ans


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        answer = solve(n, board)
        print(f"#{test_case} {answer}")


if __name__ == "__main__":
    main()