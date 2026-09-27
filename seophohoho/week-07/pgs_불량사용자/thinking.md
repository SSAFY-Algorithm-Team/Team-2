# 불량 사용자 — 풀이 사고 흐름

## 1. 제한사항부터 본다

- `user_id`는 최대 8개, `banned_id`도 최대 8개다.
- banned 칸 하나에 사용자 한 명씩 붙인다. 같은 사람은 두 번 못 쓴다.
- 경우의 수는 최대 8 × 7 × … × 1 = 8! = 40,320이다.
- 파이썬은 1초에 약 1,000만~2,000만 번 돈다(C++ 기준 어림값 "1억 번"은 파이썬엔 과하다). 한 경우당 글자 비교 8번을 쳐도 약 32만 번이라 넉넉하다. 그러니 **완전 탐색(brute force)** 으로 충분하다.
  - 완전 탐색: 가능한 경우를 전부 다 해 보는 것.

> 왜 `user_id`를 기준으로 봤나: 답은 "누구를 제재하느냐"이고, 그 후보가 전부 `user_id` 안에 있다.

## 2. 놓치기 쉬운 조건을 찾는다

- "순서만 다르고 내용이 같으면 하나로 센다."
- 예제 2에서 `*rodo`, `*rodo`는 (frodo, crodo)로도, (crodo, frodo)로도 짝지을 수 있다. 하지만 이 둘은 한 가지로 센다.
- 그래서 **순서 없는 중복 제거**가 필요하다.

## 3. 유형을 정한다

- **백트래킹(backtracking)**: 하나씩 골라 보다가 끝나거나 막히면, 한 칸 되돌아가서 다른 걸 고르는 방법.
- 보통 **DFS(깊이 우선 탐색)** 로 구현한다.
  - DFS: 한 갈래를 끝까지 판 다음에 돌아오는 탐색.
- **가지치기(pruning)**: 답이 될 수 없는 게 확실하면 그 아래는 아예 탐색하지 않는 것.
- 중복 제거는 **집합(set)** 으로 한다.

### 완전 탐색과 백트래킹의 관계

| 방식                 | 동작                                           |
| -------------------- | ---------------------------------------------- |
| 순열(`permutations`) | 모든 줄 세우기를 끝까지 만든 **뒤에** 검사한다 |
| 백트래킹             | 만드는 **도중에** 안 맞으면 바로 끊는다        |

둘 다 완전 탐색이다. 백트래킹은 가지치기를 붙인 완전 탐색이다.

## 4. 나무로 그려 본다 (예제 1: `["fr*d*", "abc1**"]`)

```
시작 (1번 칸: fr*d*)
├─ frodo  ✓ → 2번 칸: abc1**
│   ├─ fradi   ✂
│   ├─ crodo   ✂
│   ├─ abc123  ✓ → {frodo, abc123}
│   └─ frodoc  ✂
├─ fradi  ✓ → 2번 칸: abc1**
│   ├─ frodo   ✂
│   ├─ crodo   ✂
│   ├─ abc123  ✓ → {fradi, abc123}
│   └─ frodoc  ✂
├─ crodo  ✂ (c ≠ f)
├─ abc123 ✂ (길이 다름)
└─ frodoc ✂ (길이 다름)

결과 set 크기 = 2
```

- 층 하나 = banned 칸 하나.
- ✂ = 가지치기. 그 아래로는 내려가지 않는다.
- frodo 가지를 다 보고 위로 **되돌아와서** fradi 가지를 본다. 이게 백트래킹이다.

## 5. 풀이 뼈대를 말로 쓴다

1. 아이디와 패턴이 맞는지 검사한다. 길이가 같아야 하고, `*`가 아닌 자리는 글자가 같아야 한다.
2. DFS를 banned 0번 칸부터 시작한다. 지금 칸에 맞고 아직 안 뽑은 사람을 하나 고른 뒤 다음 칸으로 간다.
3. 마지막 칸까지 다 채우면, 뽑은 사람 묶음을 결과 set에 넣는다.
4. 다음 칸에서 돌아오면 뽑은 사람을 다시 뺀다.
5. 끝나면 set 크기를 답으로 낸다.

## 6. 함정을 확인한다

1. 묶음에 순서가 남아 있으면 중복이 안 걸러진다. 예제 2의 답이 4로 나온다.
2. 리스트는 **해시 불가(unhashable)** 라서 set에 넣을 수 없다.
   - 해시 불가: 내용이 바뀔 수 있어서 set이 값을 기억해 둘 수 없다는 뜻.
3. 길이 검사를 빼먹으면 `fr*d*`와 `frodoc`이 맞다고 나온다.
4. 되돌아올 때 뽑은 사람을 빼지 않으면 다른 경우를 못 본다.
5. 같은 사람을 두 칸에 넣으면 안 된다.

## 7. 코드로 옮긴다

### 7-1. 중첩 함수 버전

`dfs`가 `solution`의 변수를 **클로저(closure)** 로 바로 쓴다.

- 클로저: 안쪽 함수가 바깥 함수의 변수를 기억해서 쓰는 것.

```python
def solution(user_id, banned_id):
    def match(user, pattern):
        if len(user) != len(pattern):
            return False
        for u, p in zip(user, pattern):
            if p != '*' and u != p:
                return False
        return True

    result = set()
    used = [False] * len(user_id)

    def dfs(depth, picked):
        if depth == len(banned_id):
            result.add(frozenset(picked))
            return
        for i, user in enumerate(user_id):
            if used[i] or not match(user, banned_id[depth]):
                continue
            used[i] = True
            picked.append(user)
            dfs(depth + 1, picked)
            picked.pop()
            used[i] = False

    dfs(0, [])
    return len(result)
```

### 7-2. 함수를 밖으로 뺀 버전

- 전역 변수는 쓰지 않는다. 테스트 케이스끼리 값이 섞일 수 있어서다.
- 상태는 전부 인자로 넘긴다. 리스트와 set은 **참조(reference)** 로 넘어가서, 안에서 바꾸면 바깥에도 반영된다.
  - 참조: 복사본이 아니라 원본을 가리키는 주소.

```python
def match(user, pattern):
    if len(user) != len(pattern):
        return False
    for u, p in zip(user, pattern):
        if p != '*' and u != p:
            return False
    return True


def dfs(depth, user_id, banned_id, used, picked, result):
    if depth == len(banned_id):
        result.add(frozenset(picked))
        return
    for i, user in enumerate(user_id):
        if used[i] or not match(user, banned_id[depth]):
            continue
        used[i] = True
        picked.append(user)
        dfs(depth + 1, user_id, banned_id, used, picked, result)
        picked.pop()
        used[i] = False


def solution(user_id, banned_id):
    result = set()
    used = [False] * len(user_id)
    dfs(0, user_id, banned_id, used, picked=[], result=result)
    return len(result)
```

### 7-3. 최종 버전 (짧게, `frozenset`·`zip` 없이)

- `used` 배열 대신 `user in picked`로 이미 뽑았는지 확인한다. 최대 8명이라 충분히 빠르다.
- `frozenset` 대신 `tuple(sorted(picked))`를 쓴다. 정렬해서 순서를 없애고, 튜플로 바꿔서 set에 넣을 수 있게 만든다. 이렇게 정렬로 형태를 하나로 맞추는 걸 **정규화(canonicalization)** 라고 한다.

```python
def match(user, pattern):
    if len(user) != len(pattern):
        return False
    for i in range(len(user)):
        if pattern[i] != '*' and user[i] != pattern[i]:
            return False
    return True


def dfs(depth, user_id, banned_id, picked, result):
    if depth == len(banned_id):
        result.add(tuple(sorted(picked)))
        return
    for user in user_id:
        if user in picked or not match(user, banned_id[depth]):
            continue
        picked.append(user)
        dfs(depth + 1, user_id, banned_id, picked, result)
        picked.pop()


def solution(user_id, banned_id):
    result = set()
    dfs(0, user_id, banned_id, [], result)
    return len(result)
```

## 한 줄 결론

작은 입력(N ≤ 8)이라 **백트래킹 + 가지치기**로 완전 탐색하고, 순서만 다른 결과는 **정규화**해서 set으로 중복을 없앤다.
