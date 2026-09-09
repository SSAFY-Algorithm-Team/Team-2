T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    # 일단 먼저 5 : 2,4 이렇게 다음에 있는 숫자? 나보다 큰 것들을 싹다 넣고 만든 다음
    # 1~6까지 사람들의 그걸 만들었으면 
    # 다른 숫자의 해당 그 값들에 자신이 있으면 count+1
    # 그래서 자기가 가지고 있는 자기보다큰값 + count가 만약에 5(n-1)일 경우 정확한 것임
    # 아마도..

    N = int(input())
    M = int(input())
    information = {}
    for i in range(M):
        a,b = map(int,input().split())
        if a not in information.keys():
            information[a] = {b}
        else:
            information[a].add(b)

    def keep(i):
        # i에서 도달 가능한 모든 노드를 한 번의 순회로 모음 (중복 재탐색 방지)
        visited = set()
        stack = list(information.get(i, ()))
        while stack:
            j = stack.pop()
            if j in visited:
                continue
            visited.add(j)
            if j in information:
                stack.extend(information[j])
        if i not in information:
            information[i] = set()
        information[i].update(visited)

    for i in list(information.keys()):
        keep(i)
    # print(information)
    # print(information)

    cnt = [0] * (N + 2)
    for s in information.values():
        for x in s:
            cnt[x] += 1

    for i in range(1, N + 1):
        count = cnt[i]
        if i in information.keys():
            # print("이친구는 자기것도 있슴")
            count += len(information[i])
        if count >= N - 1:
            # print(i,"#############하나찾음!!")
            result += 1

    print(f"#{test_case} {result}")