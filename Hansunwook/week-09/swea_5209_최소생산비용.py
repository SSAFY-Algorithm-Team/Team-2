T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  result = 0
  #초기 접근
  # 일단 하나 잡고 다은꺼 하나 선택해서 최소 구하는 식으로 구현
  # dfs
  N = int(input())
  arr = []
  visit = [False]*N
  min_cost = [10000]
  for i in range(N):
    arr.append(list(map(int,input().split())))
  def dfs(count,cost):
    if count >= N:
      # print("하나 완료!!!!")
      if cost < min_cost[0]:
        # print("바뀜!")
        min_cost[0] = cost
      return
    if cost > min_cost[0]:
      return
    #print(count,"번째 생산공장 일하는중...")
    for i in range(N):
      # print(i,"번째 일 하기 가능?")
      if visit[i]:
        continue
      # print("일하기 가능 부여된 비용 증가",arr[count][i])
      visit[i] = True
      cost += arr[count][i]
      dfs(count+1,cost)
      visit[i] = False
      cost -= arr[count][i]
  dfs(0,0)
  result = min_cost[0]
  print(f"#{test_case} {result}")
