def check(user, pattern):
    if len(user) != len(pattern):
        return False
    for i in range(len(user)):
        if pattern[i] != '*' and user[i] != pattern[i]:
            return False
    return True


def dfs(depth, user_id, banned_id, picked, result):
    if depth == len(banned_id):
        picked_set = set(picked)
        if picked_set not in result:
            result.append(picked_set)
        return
    for user in user_id:
        if user in picked or not check(user, banned_id[depth]):
            continue
        picked.append(user)
        dfs(depth + 1, user_id, banned_id, picked, result)
        picked.pop()


def solution(user_id, banned_id):
    result = []
    dfs(0, user_id, banned_id, [], result)
    return len(result)