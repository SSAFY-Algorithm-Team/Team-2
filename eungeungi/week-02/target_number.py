def dfs(index, cur_sum, numbers, target):
    if index == len(numbers):
        return 1 if cur_sum == target else 0
    
    return (dfs(index+1, cur_sum + numbers[index], numbers, target) +
           dfs(index+1, cur_sum - numbers[index], numbers , target))
def solution(numbers, target):
    return dfs(0, 0, numbers, target)