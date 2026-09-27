# 똑같은 셀(A또는 B)이 K개 이상 같은 row에 연속해서 있어야함
 
def examination(lst): #복사해서 써야할듯

    flag=True
    for c in range(W): #마지막에 한 번 못오는구나
        if(not flag):
            return False
        
        for r in range(R-K+1):
            flag=False
            lst_inter=[]
            for r_row in range(r,r+K):                
                lst_inter.append(lst[r_row][c])
            
            if(lst_inter==[0]*K or lst_inter==[1]*K):
                flag=True
                break

    return flag

#대충 번호 num으로 다 채우는 함수

def make_shot(lst,row,num):

    for col in range(W):
        lst[row][col]=num

    return
    
def dfs(lst,row,depth,k):

    global ans

    if(examination(lst)):
        ans=min(ans,k)
        return
    
    if(k>=ans):
        return
 
    if(depth>=W):
        return


    for r in range(row,R):
        
        original=lst[r][:]

        for num in (0,1):
            make_shot(lst,r,num)
            dfs(lst,r+1,depth+1,k+1)
        lst[r]=original[:]
                

T = int(input())

for test_case in range(1,T+1):

    ans=10**9

    R, W, K = map(int,input().split())

    lst=[list(map(int,input().split())) for _ in range(R)]

    dfs(lst,0,0,0)

    print(f"#{test_case} {ans}")

    

    