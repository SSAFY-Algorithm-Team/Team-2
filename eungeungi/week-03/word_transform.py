from collections import deque
def solution(begin, target, words):
    cnt = 0
    mini = float('inf')
    
    queue = deque()
    queue.append((begin,0))
    visited = [False] * len(words)
    
    def differ(word1,word2):
        diff = 0
        for w in range(len(word2)):
            if diff>=2:
                return False
            if word1[w] != word2[w]:
                diff +=1
        if diff == 1:
            return True
        return False
    
    while queue:
        cur, score = queue.popleft()
        for i in range(len(words)):
            if not visited[i] and differ(cur,words[i]):
                visited[i] = True
                nxt_score= score + 1
                if words[i] == target:
                    return nxt_score
                queue.append((words[i],nxt_score))
                
        
    return 0