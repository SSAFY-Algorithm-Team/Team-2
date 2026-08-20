def solution(people, limit):
    answer = 0
    # 정렬 해서 가장 큰걸로 선택,
    # 가장 큰거에서 가장 작은거 더하기?
    # 최대 2명이라서 가능할듯?
    # 안되면 +1 하고 그냥 다음꺼 선택하면 될듯
    # 그러면 안될 경우 가장 작은게 달라지니깐 따로 변수 놓아서 되면 증가, 안되면 그대로?
    people.sort(reverse=True)
    c = 1
    i = 0
    while(len(people)-c >= i and i <= len(people)):
        # print(i)
        # print(c)
        if people[i] + people[len(people)-c] <= limit:
            # print("together", people[i], people[len(people)-c])
            c += 1
            answer += 1
        else:
            # print("just",people[i])
            answer += 1
        i += 1
    return answer