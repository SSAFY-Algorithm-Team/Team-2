# SWEA 1267 작업순서
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18TrIqIwUCFAZN&categoryId=AV18TrIqIwUCFAZN&categoryType=CODE&problemTitle=1267&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 1h


import sys
from collections import deque
sys.stdin = open('1267_input.txt', 'r')


def solve():

    # 시작 노드(진입 차수가 0인 노드) 모두 queue에 넣기
    queue = deque() # 앞으로도 진입차수가 0인 노드들만 넣어서 사용할거임!!
    for v in range(1, V + 1): # 노드 번호, 진입차수
        if in_degree[v] == 0:
            queue.append(v)

    ordered = [] # 정렬된 값 담을 공간
    while queue:
        # 진입 차수가 0인 요소 꺼내서 ordered에 삽입 (정렬의 첫 순서가 됨)
        v = queue.popleft() 
        ordered.append(v)

        # 지금 정렬된 노드에 연결된 노드들 탐색
        for node in graph[v]:
            # 앞의 노드가 하나 빠졌으니, 연결된 노드들의 진입차수도 1씩 감소
            in_degree[node] -=1 
            # 감소해서 진입차수가 0이 된 노드들은 queue에 삽입할 수 있음
            if in_degree[node] == 0:
                queue.append(node)

    return ordered
    

for tc in range(1, 11):
    V, E = map(int, input().split())
    tmp_list = list(map(int, input().split()))

    graph = {i: [] for i in range(1, V + 1)}
    in_degree = [0] * (V + 1)
    for i in range(0, 2 * E - 1, 2):
        s = tmp_list[i]
        e = tmp_list[i + 1]
        graph[s].append(e)
        in_degree[e] += 1

    ans = solve()
    print(f"#{tc}", end=" ")
    print(*ans)



########################
# 위상정렬 구현 블로그 참고
# 개념
# https://m.blog.naver.com/ndb796/221236874984
# 파이썬 구현
# https://seanpark11.tistory.com/131