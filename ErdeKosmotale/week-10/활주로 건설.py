
# 못 풀었어......

T = int(input())

for test_case in range(1, T + 1):

    N , X = map(int,input().split())

    lst = [list(map(int,input().split())) for _ in range(N)]

    #가로 체크

    for lst_width in lst:

        lst_im = lst_width[:]

        for i in range(N):

                