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

    def keep(j):
        if j in information.keys():
            information[i].update(information[j])
            for k in list(information[j]):
                keep(k)
        return
    for i in list(information.keys()):
        #다시 안돌면 업데이트된 노드에서 또 연결된 부분을 못찾는 부분이 있어 끝까지 찾을 수 있도록 구현하게
            #추가함.......근데 너무 깊어짐 이게 되나
        for j in list(information[i]):
            keep(j) 
    # print(information)
    for i in range(1,M+1):
        count = sum(1 for s in information.values() if i in s)
        # print(i,"가 포함된 값들 개수: ",count)
        if i in information.keys():
            # print("이친구는 자기것도 있슴")
            count += len(information[i])
            # print(count)
        if count >= M-1:
            # print(i,"#############하나찾음!!")
            result += 1
    print(f"{test_case} {result}")