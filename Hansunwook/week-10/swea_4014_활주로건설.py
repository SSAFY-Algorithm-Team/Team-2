T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  result = 0
  # 초기 접근:
  # x는 그냥 되는지 안되는지 확인용
  # 완탐? 으로 한줄씩 잡고 되는지 다 확인
  N,X = map(int,input().split())
  arr = []
  for i in range(N):
    arr.append(list(map(int,input().split())))
  # 한줄씩 잡는건데.. 그냥 높은거 낮은거 신경 안쓰고

  # 낮은 부분 -> 높은 부분
  # 이건 먼저 x개 이상으로 이어져 있는지 확인한 다음(미리 저장해 두고)
  # 다음 높은 부분이 1칸 더 높다면 저장해놓은(얼마나 이어져 있는지) 게 x보다 크면 넘어가기
  # 아니면 그냥 다음으로

  # 높은 부분 -> 낮은 부분
  # 먼저 저장해둔 걸 그냥 지우고 (한칸 낮으면)거기서부터 개수 세서 x보다 더 크다면 넘어가기
  # 아니면 그냥 다음으로

  # 여기서 한가지 신경써야 하는 부분은 맨 끝이면 x 그런거 상관 없는듯..? 
  # 아마.. 일단 구현해보고 이건 나중에

  #세로줄
  result1 = 0
  for y in range(N):
    #세로니까 x,y면 x+1
    connect_count = 0
    nextx = 0
    nextmove= True
    while(nextx < N):
      #이미 안된다고 판단 되었으면 그만가
      if nextmove is False:
        break
      nowx = nextx
      nextx += 1
      if arr[nowx][y] == arr[nextx][y]:
        connect_count += 1
        continue
      else:
        # 높은 부분 -> 낮은 부분
        if arr[nowx][y] == arr[nextx][y]-1:
          
        # 높은 부분 -> 낮은 부분
        elif arr[nowx][y]-1 == arr[nextx][y]:
          
        else:
          nextmove = False

  #가로줄
  print(f"#{test_case} {result}")
