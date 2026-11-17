import sys
sys.stdin = open('3289_input.txt', 'r')


def init():
    parent = [i for i in range(N + 1)] 
    return parent


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def check(x, y): ## 여기 주의!! 마지막으로 루트 노드를 찾은 다음에 한 집합인지 아닌지 판단해야됨 -> 아래 참고
    if find(x) == find(y):
        return "1"
    else:
        return "0"
    

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    parent = init()
    result = ""
    for _ in range(M):    
        F, A, B = map(int, input().split())    
        if F:
            result += check(A, B)
        else:
            union(A, B)
        # print(parent)

    print(f"#{tc} {result}")
    

"""
[착각]
경로 압축을 쓰면 parent[x]에 항상 루트가 들어있다 → X
압축은 find를 부른 그 순간의 경로만 고친다

[예시] union(3, 7)
find(7) → 루트 6 → parent[7] = 6
그 뒤 parent[6] = 1
→ 7 → 6 → 1 (대표는 1, parent[7]은 아직 6)

[check는 find로]
parent[x] = 바로 위 부모 / find(x) = 대표
check(7, 1)
  parent 비교: 6 vs 1 → "0" (틀림)
  find 비교:   1 vs 1 → "1" (맞음)
"""