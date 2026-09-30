def solve(n, weights):
    ans = 0 # 최종 반환 경우의 수 
    is_used = [False] * n
    sum_w = sum(weights)
    # fact 계산 미리 해두기
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i


    def dfs(depth, left, right):
        nonlocal ans
        # depth = n이 되면 return
        if depth == n:
            ans += 1
            # print("!")
            return

        # 남은 추를 오른쪽에 올려도 right가 left를 넘지 않는 경우, 경우의 수로 더해버리기 -> 그리고 종료
        if 2 * left >= sum_w: # left >= right + remain_w // remain_w = sum_w - left - right
            remain_n = n - depth
            ans += fact[remain_n] * (2 ** remain_n)
            return
        

        for i in range(n):
            if not is_used[i]:
                is_used[i] = True
                dfs(depth + 1, left + weights[i], right)
                if left >= right + weights[i]:
                    dfs(depth + 1, left, right + weights[i])
                is_used[i] = False

    dfs(0, 0, 0)
    return ans


def main():
    # start = time.time()

    # sys.stdin = open('3234_input.txt', 'r')
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        weights = list(map(int, input().split()))
        ans = solve(n, weights)
        print(f"#{tc} {ans}")
        # print(time.time() - start)


if __name__ == "__main__":
    main()
