from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    N,M = map(int,input().split())
    # 초기 접근
    # 일단 음...큰수를 2로 계속 나눠서 나머지 나올때까지 나누고
    # 7 -> 3(+1) -> 1(+1) 이렇게 해서 하면 되지 않을까..
    # 근데 -10이 변수임..
    # 으으으으음
    # -10이 쓰일 경우는 N이 더 클 경우에인가
    # 그러면 N이 더 크면 10의자리수 + 1의자리수 더하기 해서 결과

    # -> 최종 결론
    # M이 더 클 경우에는 M을 2로 나눠서 업데이트, 1 될때까지 몇번 나눴는지
    # +) 업데이트 할 경우 홀수면 +1
    # N이 더 클 경우에는 10의자리수 + 1의자리수 더하기
    # #구현
    # if N > M:
    #     result = ((N-M)//10) + ((N-M)%10)
    #     print("N이 더 큼",N,M,": ",result)
    # #N이랑 M이 같은 경우는 없다고 했음
    # else:
    #     nown = M
    #     count = 0
    #     while(nown - N >= 1):
    #         print("지금 숫자는: ",nown)
    #         print("지금 count는: ",count)
    #         count += 1
    #         nown //= 2
    #         if nown - N <= 1:
    #             break
    #         #만약 홀수면 +1 해야함
    #         if nown%2 == 1:
    #             print("+1") 
    #             count += 1
    #     #끝나고 nown이 1인지 0인지에 따라 결과 다름?
    #     print("####끝남, nown은 ",nown,"count는 ",count)
    #     result = count + nown - N 
    #     print("M이 더 큼",N,M,": ",result)


    # -> 기각..
    # 반례 계속 나와서 bfs로 바꿈
    
    print(f"#{test_case} {result}")