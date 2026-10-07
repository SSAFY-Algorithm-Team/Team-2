# 5247 SWEA 연산
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWUS1FaKImUDFAVT&categoryId=AWUS1FaKImUDFAVT&categoryType=CODE&problemTitle=5247&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 시간 2h 시도 4

"""
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
사용할 수 있는 연산 : +1, -1, *2, -10 
최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램
연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
"""

"""
DFS
- 연산 횟수가 best보다 커지면 가지치기 
- 100만 넘으면 종료 (1000010.. ?) ==> 최종 목적지인 M보다도 (10이상: 반례 존재) /(2배 ??) 커지면....의미 없지 않나
                                    (반례 ?) 2 -> 5 / 2 * 2 - 1 
                                            10 -> 29 / 10 * 2 * 2 - 10 - 1
- 0보다 작아지면 종료
- 최종 목적지보다 2배 크면 의미 없다 ? 
-> max recursion !!!!!!!!!!!!
"""

"""
BFS
- 한 곳으로 깊게 들어가보지 말고, 여러 계산해보다가 m에 도달하면 return
- 시간 복잡도가 훨씬 적음 (현재까지 계산에서 **가장 작은 cnt**로 유지되며, m인 순간 출력되므로)
"""


import sys
from collections import deque

sys.stdin = open('5247_input.txt', 'r')


OP = ["*2", "+1", "-10", "-1"]


def calc(curr, op):
    if op == "+1":
        return curr + 1
    elif op == "-1":
        return curr - 1
    elif op == "*2":
        return curr * 2
    elif op == "-10":
        return curr - 10


def search(n, m):

    queue = deque([(n, 0)])
    nums[n] = 1

    while queue:
        # print(stack)
        curr, cnt = queue.popleft()
        for op in OP:
            calculated = calc(curr, op)
            if 0 < calculated <= 1000000 and not nums[calculated]: 
                queue.append((calculated, cnt + 1))
                nums[calculated] = 1
                # 계산된 숫자에 해당하는 index는 표시해주기 -> 이미 더 작거나 같은 cnt로 계산한 값임
                if calculated == m:
                    return cnt + 1

    return -1


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    nums = [False] * 1000001
    cnt = search(n, m)
    print(f"#{tc} {cnt}")


"""
DFS 시도, max recursion !!

import sys
sys.stdin = open('5247_input.txt', 'r')


OP = ["*2", "+1", "-10", "-1"]


def calc(curr, op):
    if op == "+1":
        return curr + 1
    elif op == "-1":
        return curr - 1
    elif op == "*2":
        return curr * 2
    elif op == "-10":
        return curr - 10


def search(curr, cnt):
    global m, best

    # print(curr)

    if cnt >= best:
        return

    if curr > 1000000 or curr > m + 10 or curr < -10:
        return

    if curr == m:
        best = cnt
        return

    for op in OP:
        # print(op, curr)
        calculated = calc(curr, op)
        search(calculated, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    # if tc == 1:
    n, m = map(int, input().split())
    best = float('inf')
    search(n, 0)
    print(f"#{tc} {best}")
"""