# 프로그래머스 43163 단어변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 시간 36m / 시도 2

from collections import deque

def compare(word1, word2):
    diff = 0 
    n = len(word1)

    for i in range(n):
        if word1[i] != word2[i]:
            diff += 1

    if diff == 1:
        return True
    else:
        return False
    

def solution(begin, target, words):
    if target not in words: # 타겟 단어가 리스트에 없는 경우 -> 예외
        return 0

    n = len(words)
    is_used = [False] * n
    queue = deque([(begin, 0)])

    while queue:
        # print(queue)
        w, d = queue.popleft()
        if w == target: # bfs는 항상 종료조건 넣는 위치가 헷갈림 => 여기보다 좋은 자리 없나? (target word가 맨 왼쪽에 오면 종료되는데, 등장하면 종료시킬 수?)
            return d

        for i, word in enumerate(words):
            if not is_used[i] and compare(word, w):
                queue.append((word, d + 1))
                is_used[i] = True
    return 0