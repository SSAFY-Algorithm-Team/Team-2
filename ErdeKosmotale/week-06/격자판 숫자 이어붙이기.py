T=int(input())

DIRECTION=[(-1,0),(1,0),(0,-1),(0,1)]

def dfs(row,col,num_str):

    global set_ans

    num_str += (str(lst[row][col]))

    if(len(num_str)==7):
        set_ans.add(num_str)
        return


    for r,c in DIRECTION:
        n_row = row+r
        n_col = col+c

        if(0<=n_row<4 and 0<=n_col<4):
            dfs(n_row,n_col,num_str)            
            

for test_case in range(1,T + 1):

    ans=0

    lst=[list(map(int,input().split())) for _ in range(4)]
    
    set_ans=set()

    for r in range(4):
        for c in range(4):
            t=dfs(r,c,'')

    ans=len(set_ans)



    print(f"#{test_case} {ans}")
