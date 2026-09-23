
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

for test_case in range(1,T+1):
    N=int(input())

    lst=[list(map(int,input().split())) for _ in range(N)]

    lst_stair=[]
    lst_people=[]

    for r in range(N):
        for c in range(N):
            if(lst[r][c]==1):
                lst_people.append((r,c))
            elif(lst[r][c]>=2):
                lst_stair.append((r,c))

    
    print(combination(3))