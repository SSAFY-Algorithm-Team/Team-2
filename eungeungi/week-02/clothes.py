def solution(n, lost, reserve):
    maxi = 0
    cnt = 0
    lost.sort()
    reserve.sort()
    overlap = set(lost) & set(reserve)
    lost = [x for x in lost if x not in overlap]
    reserve = [x for x in reserve if x not in overlap]   
    for l in lost:
        for i, r in enumerate(reserve):
            if abs(l-r) <=1:
                cnt+=1
                reserve.pop(i)
                break

    result = n - len(lost) +cnt
    return result