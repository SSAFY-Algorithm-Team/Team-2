T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = [0]
    #초기접근
    #일단 N이 작아서 거의 다 될텐데..
    #그러면 N*N 배열 만들고 거기에 완탐으로 다 넣어보기??
    #그냥 퀸 문제도 안풀어봐서 감을 못잡겠
    #하나를 놓으면 남는 자리가 나오고 거기에 또 하나 놓고 dfs인가..
    # -> 클로드한테 힌트달라 했음
    # 같은 열에는 무조건 들어갈 수 없으니까 전체 하지 말고
    # 열을 하나 잡아서 백트레킹 돌리라는 힌트를 받았음
    # -> 구현..
    N = int(input())
    arr = []
    for i in range(N):
      arr.append([])
    #놓을 수 있는지 없는지 확인
    #이미 count 증가하면서 같은 층은 안겹치기 때문에 검증 안해도 됨
    # 그래서 같은 대각선인지랑 밑에 있는지만 확인하면 됨
    def can_put(a,b):
        # print("queen 위치: ",queen)
        # print("놓아보는중...",a,b)
        for count,i in queen:
            if i == b:
                return False
            #대각선 확인 방법 생각 안나서 클로드한테 물어봄
            # 행 차이의 절댓값 == 열 차이의 절댓값 이면 대각선이라고 했음
            if abs(a-count) == abs(b-i):
                return False
        # print("통과!!!!!!")
        return True 
    #퀸 자리
    queen = []
    def dfs(count):
      if count >= N:
        # print("###########체스판 하나 완료")
        result[0] += 1
        return
      for i in range(N):
        if can_put(count,i):
          queen.append([count,i])
          dfs(count+1)
          queen.pop()
        else:
          continue
    dfs(0)
    print(f"#{test_case} {result[0]}")