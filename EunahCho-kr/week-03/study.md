## 발표용
### 프로그래머스 Lv3. 여행경로
###### https://school.programmers.co.kr/learn/courses/30/lessons/43164
---
접근법 
1. 티켓 정렬 (뒷 원소에 기준) - (다음에 오는 원소가 알파벳 순으로 출력되어야 함)
2. dfs : 아직 사용하지 않은 티켓, path의 마지막 원소 = 티켓의 첫 원소면 depth + 1
    - 종료 조건은 depth = n - 1일 때 => answer 출력
    - 가장 깊이 들어갔다면 dfs에서 아예 나옴 (flag 활용) => 아니라면 백트래킹으로 하나씩 나오고 다음 경우 확인
        - 주어진 티켓을 모두 사용해야 하므로 종료 조건이 depth = n - 1
        - 갈 수 있는 곳이 두 곳 이상일 때는 알파벳 순이므로, 첫번째 정답이 나오면 dfs 나와버림
3. 인천 출발인 티켓 다 탐색
    - 이때도 첫 정답이 나오면 return 해버림
---

```
def solution(tickets):
    tickets.sort(key = lambda x: x[1])
    # print("ticekets", tickets)
    n = len(tickets)
    is_used = [False] * n
    flag = False
    answer = []

    def dfs(depth):
        nonlocal answer, flag
        # print(depth," / ",path)
        if depth == n - 1:
            answer = path[:]
            flag = True # 깊이의 가장 끝까지 간 경우 true
            return answer
        
        for i in range(n):
            if not is_used[i] and tickets[i][0] == path[-1]:
                is_used[i] = True
                path.append(tickets[i][1])
                dfs(depth + 1)
                
                if flag: # 길이에 맞는 첫 번째 애가 정답임 => 함수가 지정 길이에 도달했으면 break
                    break
                    
                is_used[i] = False
                path.pop()

    for i in range(n): # 인천 출발
        # print("인천 있는 티켓 탐색 : ", i)
        path = ["ICN"] # 변수 초기화
        if tickets[i][0] == "ICN":
            path.append(tickets[i][1])
            is_used[i] = True
            dfs(0)
            is_used[i] = False # dfs 끝나면 원래대로 돌려주기
            if flag: # dfs 끝까지 돌렸을 때(= 길이가 n + 1일 때)만 출력 -> 아니면 다음 반복문
                return answer
```
----
## 스터디에서 배운거 !

### 햄버거 다이어트
- 면접 빈출 개념 : 0-1knapsack 
```
dp[i][j] = 1 ~ i번째 물품 중, j무게 내에서 최대 가치
    -> dp[n][k] 출력
-> k무게에서 최대 가치를 탐색하고 싶다면,
(k 무게 - i번째 물품 무게)까지 최대 가치 + i번째 물품 최대 가치 VS i-1번째 물품까지, k무게 이내 최대 가치
```
### 단어변환
- 응선) from collections import defaultdict  
  - 프로그래머스 테케에 없는 엣지 케이스 (log - lot - lok - log ) 누적 연산 안하고 한번에 갈 수 잇는  
- 승섭 - 인접리스트, bfs

``` 
# 응선 - 엣지케이스
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
```

 ## 홈 방범 서비스
 - 선욱 : bfs 안쓰고 풀 수 있음
```
T = int(input())
for test_case in range(1, T + 1):
    result = 0
    N,M = map(int,input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int,input().split())))
    # 초기 접근
    # K 만족하는지 확인하고 만족하는 최대 K 출력
    # 만족하는 범위의 집인지 확인하는 방법은 
    # -> 만약 a,b 중심일 경우 c,d에 집이 있으면 (a-c)^2+(b-d)^2 이 K^2 보다 작거나 같을 경우 안에 들어온다.
    # 그러므로 각 중심이 변할 떄 마다 업데이트 하고 해당되는 수를 센다
    houses = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 1]
    best = 0
    for r in range(N):
        for c in range(N):
            print("만약 중앙값이 ",r,c,"라면")
            dists = sorted(abs(r - i) + abs(c - j) for i, j in houses)
            print("거리: ", dists)
            # 거리 d를 포함하려면 K-1 >= d, 즉 K >= d+1
            for cnt in range(1, len(dists) + 1):
                # cnt번째로 가까운 집의 거리
                d = dists[cnt - 1]
                # 이 집을 포함하는 최소 K          
                K = d + 1                    
                cost = K * K + (K - 1) * (K - 1)
                profit = cnt * M - cost
                if profit >= 0 and cnt > best:
                    best = cnt
    result = best
    
    print(f"#{test_case} {result}")
  ```