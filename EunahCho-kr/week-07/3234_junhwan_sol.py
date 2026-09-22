import sys
import time
from math import factorial


def dfs(depth, left, right, remain):
    global cnt
    if depth == N:
        cnt += 1
        return
    if left - right >= remain:     
        k = N - depth
        cnt += factorial(k) * (2 ** k)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        dfs(depth + 1, left + arr[i], right, remain - arr[i])    
        if left >= right + arr[i]:                              
            dfs(depth + 1, left, right + arr[i], remain - arr[i])
        visited[i] = False


start = time.time()
sys.stdin = open('3234_input.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * N
    cnt = 0
    dfs(0, 0, 0, sum(arr))
    print(f'#{tc} {cnt}')
    print(time.time() - start)