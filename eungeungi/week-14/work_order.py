1 : (4)
2 : (1)
3 : (2)
4 : ()
5 : (1,8)
6 : (5,7)
7 : (2)
8 : ()
9 : (8)

# value가 없는 값들을 answer에 넣기
# 각 키 값에서 answer에 있는 value값 빼기
# 다시 value가 없는 값들 answer에 넣기
# 다시 각 키값에서 answer에 있는 value값 빼기 - visited로 전에 있던 값은 제외
# 반복해서 하기
from collections import defaultdict, deque
def find(ls,V):
    visited = [False] * (V+1)
    answer = []
    for i in range(1,V+1):
        if len(ls[i]) ==0:
            answer.append(i)
            visited[i] = True
    while len(answer) <V:
        for i in range(1,V+1):
            if not visited[i] and all(visited[x] for x in ls[i]):
                answer.append(i)
                visited[i] = True
    return answer


for tc in range(1,11):
    V, E = map(int, input().split())
    arr = list(map(int,input().split()))
    ls = defaultdict(list)
    for i in range(0,E*2,2):
        ls[arr[i+1]].append(arr[i])
    ans = find(ls,V)
    print(f"#{tc}", *ans)
