def solution(numbers, target):
    answer = 0
    #초기 접근
    #일단 전체 경로 확인해야 해서 dfs가 낫지 않을까 라는 생각
    # 그러면 전체 끝까지 돌리고 끝까지 갔을 경우 타겟이면 result +1
    mul = [-1,1]
    N = len(numbers)
    num = [0]
    result = [0]
    def dfs(count):
        if count == N:
            # print("###########한줄 생성 완료")
            if num[0] == target:
                # print("타겟임")
                result[0] += 1
            return
        for i in range(2):
            num[0] += mul[i]*numbers[count]
            dfs(count+1)
            num[0] -= mul[i]*numbers[count]
    dfs(0)
    answer = result[0]
    
    return answer