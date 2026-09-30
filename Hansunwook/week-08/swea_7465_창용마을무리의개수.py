T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    #초기접근
    # 뭐든 두개중에 숫자가 같은 부분이 있으면 같은 무리라고 치기 때문에
    # 배열에 같은게 있으면 거기에 넣고 아니면 새로 만들어서 넣기?
    # 마지막에 각 배열마다 같은 값이 있다면 합치는걸로 가도 될..까
    N,M = map(int,input().split())
    arr = []
    for i in range(N+1):
        arr.append([])
    for i in range(M):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    # print(arr)
    visit = [False]*(N+1)
    count = 0
    for i in range(1,N+1):
      # print(i,"번째 값 확인하는중...")
      if visit[i] != True:
        visit[i] = True
        count += 1
      st = [i]
      while(st):
        a = st.pop()
        for j in arr[a]:
          if visit[j]:
            continue
          visit[j] = True
          st.append(j)
      result = count
    print(f"#{test_case} {result}")