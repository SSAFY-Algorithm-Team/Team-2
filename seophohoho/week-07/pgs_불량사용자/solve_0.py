def match(user, pattern):
    if len(user) != len(pattern):
        return False
    for i in range(len(user)):
        if pattern[i] != '*' and user[i] != pattern[i]:
            return False
    return True


def solution(user_id, banned_id):
    n = len(user_id)
    k = len(banned_id)
    result = set()
    for num in range(n ** k):
        idx = []
        for _ in range(k):
            idx.append(num % n)
            num //= n
        if len(set(idx)) != k:
            continue
        ok = True
        for j in range(k):
            if not match(user_id[idx[j]], banned_id[j]):
                ok = False
                break
        if ok:
            result.add(tuple(sorted(idx)))
    return len(result)