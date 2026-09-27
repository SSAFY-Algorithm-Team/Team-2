def solution(info, query):
    # info를 array로 받음
    info_arr = [line.split() for line in info]

    # query도 array로 받음
    query_arr = []
    for line in query:
        tmp = []
        for string in line.split(" "):
            if string != "and":
                tmp.append(string)
        query_arr.append(tmp)
    # print(info_arr, query_arr)
    
    # query의 맨 윗줄 부터 -> info에 왼쪽 부터 해당하는 idx번호 저장
    n = len(query_arr) # 세로 길이
    m = len(query_arr[0]) # 가로 길이
    answer = []

    for line in query_arr:
        mask = [[False] * m for _ in range(n)]
        for idx, obj in enumerate(line):

            if idx == m - 1:
                for jdx in range(n):
                    if int(info_arr[jdx][idx]) >= int(obj):
                        mask[jdx][idx] = True

            if obj == "-":
                for jdx in range(n):
                    mask[jdx][idx] = True
            else:
                for jdx in range(n):
                    if info_arr[jdx][idx] == obj:
                        mask[jdx][idx] = True


        for row in mask:
            print(row)
        print()

        cnt = 0
        for line in mask:
            if sum(line) == m:
                cnt += 1

        answer.append(cnt)

    
    # 조건에 걸러지는 idx는 삭제
    # idx 길이 출력
    return answer


ans = solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], 
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])

print(ans)