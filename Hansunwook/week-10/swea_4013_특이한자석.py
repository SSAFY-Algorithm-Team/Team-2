TC = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, TC + 1):
  result = 0
  T = int(input())
  arr = []
  for i in range(4):
    arr.append(list(map(int,input().split())))
  # 먼저 회전하면 끝 위치만 업데이트 하는 식으로 구현
  # 맨위 부분을 업데이트하기(그냥 배열 전체 안움직이고 위치 이동해서)
  # 0번째에서 -> 1번째 이런식으로

  #초기 윗부분 위치
  numberspot = [0,0,0,0]
  for i in range(T):
    number,numbermove = map(int,input().split())
    # 1->2 1<-2->3 2<-3->4 4 ->3
    # 양 방향으로 연쇄되는 느낌임
    #number 1부터인거 지금 발견함..그냥 -1 해주자..
    number -= 1
    afternumberspot = numberspot[:]
    afternumberspot[number] -= numbermove
    nownumber = number
    #왼쪽으로
    count = 1
    for i in range(3):
      lnumber = nownumber-1
      if lnumber < 0:
        break
      if arr[nownumber][(numberspot[nownumber]+6)%8] == arr[lnumber][(numberspot[lnumber]+2)%8]:
        break
      if arr[nownumber][(numberspot[nownumber]+6)%8] != arr[lnumber][(numberspot[lnumber]+2)%8]:
        count *= -1
        #반대쪽으로
        afternumberspot[lnumber] -= numbermove*count
        nownumber -= 1
    nownumber = number
    count = 1
    #오른쪽으로
    for i in range(3):
      rnumber = nownumber+1
      if rnumber > 3:
        break
      if arr[nownumber][(numberspot[nownumber]+2)%8] == arr[rnumber][(numberspot[rnumber]+6)%8]:
        break
      if arr[nownumber][(numberspot[nownumber]+2)%8] != arr[rnumber][(numberspot[rnumber]+6)%8]:
        count *= -1
        #반대쪽으로
        afternumberspot[rnumber] -= numbermove*count
      nownumber += 1
      #마지막으로 위치 업데이트
    numberspot = afternumberspot[:]
  result = arr[0][numberspot[0]] + arr[1][numberspot[1]]*2 + arr[2][numberspot[2]]*4 + arr[3][numberspot[3]]*8
  print(f"#{test_case} {result}")