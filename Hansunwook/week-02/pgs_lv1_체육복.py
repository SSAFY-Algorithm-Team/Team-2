def solution(n, lost, reserve):
    #초기 접근
    # 그리디로?
    # 처음부터 시작해서 도난당한 학생 앞뒤(나 포함)로 여벌 있으면 추가 후 삭제
    # 만약 여벌 학생이 도난당한 학생에 있을 경우 안됨
    #근데 음... 앞에 있는 사람부터 봐야 끝에 안남을듯?
    answer = 0
    #list(set(list1) - set(list2))
    #겹치는 부분 지우기
    lost2 = lost
    lost = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost2))
    reserve.sort()
    for i in reserve:
            # 값을 지정해서 지우고 싶을 때는 remove
            # 인덱스를 지정해서 지우고 싶을 때는 pop
        if i-1 in lost:
            lost.remove(i-1)
            continue
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n-len(lost)
    return answer