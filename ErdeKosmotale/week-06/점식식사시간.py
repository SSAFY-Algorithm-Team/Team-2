from collections import deque

def combination(r):

    path=[]
    result=[]
    n_people=len(lst_people)
    
    def backtrack(start):
        
        if(len(path)==r):
            result.append(path[:])
            return

        for i in range(start,n_people):
            path.append(i)
            backtrack(i+1)
            path.pop()

    backtrack(0)

    return result
        
T=int(input())

# 사람들을 어느 계단에 보낼지 미리 구분해놓기
# 1번 계단에 몇 초에 도착하는지 2번 계단에 몇 초에 도착하는지 표시가 가능함

def dfs(lst,K): #넘겨주는 리스트

    t=0
    idx=0
    queue=deque()

    
    while(True):

        if(idx==len(lst)):
            return t

        while(queue and queue[0]<=t):        # 나갈때가 됐을 때
            queue.popleft()
    
        if(lst[idx]+1<=t):
            if(len(queue)<3): #그냥 내려갈수 있을때
                queue.append(t+K)
                idx+=1
                continue

            else:
                 t+=1 
                 

        else:
             t+=1
             continue

    


                        
for test_case in range(1,T+1):

    ans=10**9

    N=int(input())

    lst=[list(map(int,input().split())) for _ in range(N)]

    lst_stair=[]
    lst_people=[]

    for r in range(N):
        for c in range(N):
            if(lst[r][c]==1):
                lst_people.append((r,c))
            elif(lst[r][c]>=2):
                lst_stair.append((r,c,lst[r][c]))

    row_stair1, col_stair1 = lst_stair[0][0] , lst_stair[0][1]
    row_stair2, col_stair2 = lst_stair[1][0] , lst_stair[1][1]
    
    K_stair1 = lst_stair[0][2]
    K_stair2 = lst_stair[1][2]

    for idx in range(len(lst_people)+1):        
        for result in combination(idx):             #이거 두줄 추가함
            q_stair1=[]
            q_stair2=[]
            for i in range(len(lst_people)):

                if(i in result):

                    row_i, col_i = lst_people[i]
                    distance = abs(row_stair1-row_i) + abs(col_stair1-col_i)
                    q_stair1.append(distance)
                else:
                    row_i, col_i = lst_people[i]
                    distance = abs(row_stair2-row_i) + abs(col_stair2-col_i)
                    q_stair2.append(distance)

            q_stair1.sort()
            q_stair2.sort()

            ans_inter=max(dfs(q_stair1,K_stair1)+K_stair1-1,dfs(q_stair2,K_stair2)+K_stair2-1)
            ans=min(ans,ans_inter)


    print(f"#{test_case} {ans+1}")

            
           

    

    
