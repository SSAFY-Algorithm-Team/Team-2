
def solution(k, room_number):
    ind = {}
    answer = []    
    
    def find(x):
        path = []
        while x in ind:
            path.append(x)
            x = ind[x]
        
        for p in path:
            ind[p] = x
        return x
    
    for i in range(len(room_number)):
        if room_number[i] not in ind:
            ind[room_number[i]] = room_number[i]+1
            answer.append(room_number[i])
        else:
            num = find(room_number[i])
            answer.append(num)
            ind[num] = num+1
    return answer

# 재귀 깊이 고려 X
def find(x):
    if x not in ind:
        return x
    ind[x] = find(ind[x])
    return ind[x]