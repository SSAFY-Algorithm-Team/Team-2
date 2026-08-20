### 발표
programmers 타겟 넘버 
https://school.programmers.co.kr/learn/courses/30/lessons/43165

문제 설명
- numbers, target이 주어짐
- numbers를 적절히 더하거나 빼서 target 넘버를 만들 수 있는 방법의 수 출력 

접근법
1. [1, -1]로 이루어지고, 길이가 numbers와 같은 중복 순열 생성 (dfs 이용)
2. 길이가 numbers와 같아질 때, [중복 순열 * numbers] 원소 곱 -> 합 
3. 2번 값이 target과 같다면 count

코드
```
def solution(numbers, tartget):
    arr = [-1, 1]
    m = len(numbers)
    path = []
    answer = 0
    def dfs(depth):
        nonlocal answer
        if depth == m:
            tmp = 0
            for i in range(m):
                tmp += path[i] * numbers[i]
            if tmp == tartget:
                answer += 1
            return
        
        for i in range(len(arr)):
            path.append(arr[i])
            dfs(depth+1)
            path.pop()
        return answer

    dfs(0)
    return answer
```

의문
1. nonlocal 대신 다른 변수 선언법?

---

### 다른 문제 

흠... 들으면서 추가하기