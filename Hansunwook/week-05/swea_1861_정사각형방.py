import sys
 
sys.setrecursionlimit(3000)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    #
    # 초기 접근
    # 완전 탐색으로?
    # 작은수 출력하기 위해 클경우만 바꾸기

    #
    N = int(input())
    arr = []
    udrl = [[1,0],[0,1],[-1,0],[0,-1]]
    for i in range(N):
        arr.append(list(map(int,input().split())))
    def count(startx,starty):
        a = startx
        b = starty
        # print("찾는중...",startx,starty)   
        # print("방번호: ",arr[startx][starty])
        for i in range(4):
            a += udrl[i][0]
            b += udrl[i][1]    
            if 0<=a<N and 0<=b<N:
                if arr[a][b] == arr[startx][starty]+1:
                    # print("찾음!!!!")
                    # print(startx,starty,"다음에",a,b,"로 이동...")
                    c[0] += 1
                    count(a,b)
            a -= udrl[i][0]  
            b -= udrl[i][1]      
        # print("찾기 종료 count: ",c[0])
        return 
    max = -1
    num = -1
    c = [0]
    for i in range(N):
        for j in range(N):
            # print("###########시작하는중..",i,j)
            c[0] = 1
            count(i,j)
            if max == c[0] and num > arr[i][j]:
                 num = arr[i][j]
            if max < c[0]:
                num = arr[i][j]
                max = c[0]
                # print("=====================max값 바뀜")
                # print(num,"번째 방")
                # print(max,"만큼 가기 가능")
                
    print(f"#{test_case} {num} {max}")