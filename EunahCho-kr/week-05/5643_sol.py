# 5643 키 순서
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXQsLWKd5cDFAUo
# 시도 1 / 시간 1h 20m

import sys


def find_students(n, graph):
    final_cnt = 0  # 최종 가능한 경우의 수
    for i in range(1, n + 1):
        tmp_cnt = 0  # for문 안에서 잠시 쓸
        # 해당 key로 이어지는 key들
        for j in range(1, n + 1):
            if i == j:
                continue
            if i in graph[j]:
                tmp_cnt += 1
        # 해당 key에서 갈 수 있는 value
        tmp_cnt += len(graph[i])

        if tmp_cnt + 1 == n:
            final_cnt += 1

    return final_cnt


def find_connected_nodes(n, graph):
    for key in range(1, n + 1):
        values = graph[key]
        if values:
            is_used = [False] * (n + 1)
            for val in values:
                is_used[val] = True

            for val in values:
                for v in graph[val]:
                    if not is_used[v]:
                        is_used[v] = True
                        graph[key].append(v)


def main():
    sys.stdin = open('5643_input.txt', 'r')
    t = int(input())
    for tc in range(1, t + 1):
        n = int(input())
        m = int(input())
        graph = {i: [] for i in range(1, n + 1)}
        for _ in range(m):
            key, val = map(int, input().split())
            graph[key].append(val)
        # print(graph)
        find_connected_nodes(n, graph)
        # print(graph)
        ans = find_students(n, graph)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    main()
