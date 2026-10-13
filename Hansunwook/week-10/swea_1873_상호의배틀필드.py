T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  result = 0
  #일단 시작점이 어디인지부터 알아낸 다음에 시뮬레이션
  H,W = map(int,input().split())
  maps = []
  start = ['^','v','<','>']
  nowposition = []
  nowudrl = 0
  for i in range(H):
    maps.append(list(input()))
    #여기 안에서 찾는게 빠를까 밖에서 따로 찾고 멈추는게 빠를까..
    #모름 나중에 스터디할 때 물어봐야지
    for j in range(W):
      if maps[i][j] in start:
        for k in range(4):
          if maps[i][j] == start[k]:
            nowudrl = k
        nowposition.append([i,j])
  # print(nowposition)
  # print(nowudrl)
  N = int(input())
  move = list(input())
  udrl = [[-1,0],[1,0],[0,-1],[0,1]]
  #시작 위치 찾았으면 시뮬레이션 시작하기
  def shoot(a,b):
    shoota,shootb = a,b
    while(0<=shoota<H and 0<=shootb<W):
      if maps[shoota][shootb] == "*":
        maps[shoota][shootb] = "."
        break
      if maps[shoota][shootb] == "#":
        break
      shoota += udrl[nowudrl][0]
      shootb += udrl[nowudrl][1]
  a,b = nowposition[0][0],nowposition[0][1]
  for i in move:
    if i == "S":
      shoot(a,b)
      continue
    if i == "U":
      nowudrl = 0
    elif i == "D":
      nowudrl = 1
    elif i == "L":
      nowudrl = 2
    elif i == "R":
      nowudrl = 3
    if 0<=a+udrl[nowudrl][0]<H and 0<=b+udrl[nowudrl][1]< W:
      a += udrl[nowudrl][0]
      b += udrl[nowudrl][1] 
      if maps[a][b] != "." and maps[a][b] not in start:
        a -= udrl[nowudrl][0]
        b -= udrl[nowudrl][1] 
      else:
        maps[a - udrl[nowudrl][0]][b - udrl[nowudrl][1] ] = "." 
    maps[a][b] = start[nowudrl]
  #프린트 하는법 클로드한테 물어봄...
  #어렵다... 암기하기
  print(f"#{test_case}", end=" ")   # 줄바꿈 없이 '#1 '만 출력
  for row in maps:
      print(''.join(row)) 