# 무조건 대각선으로만 이동합니다!
# dfs가 맞다 이건

DIRECTION = [(-1,1), (1,1), (1,-1), (-1,-1)]

# 현재 돌면서 먹은 디저트를 기억해야 할듯
# used_direction에 있고 now_direction이랑 다른데 한번 더 쓸수는 없음

def dfs(row,col,start_row,start_col,now_visited,used_direction,now_direction,num_desert):
    global ans

    if(num_desert != 0 and (row,col) == (start_row,start_col)):
        ans=max(ans,num_desert)
        return

    used_direction[now_direction]=1

    print(row,col)
    for next_direction in range(4):

        n_row = row + DIRECTION[next_direction][0]
        n_col = col + DIRECTION[next_direction][1]
        
        if(used_direction[next_direction] == 1 and now_direction != next_direction):
            continue

        if(n_row<0 or n_row>=N or n_col<0 or n_col>=N):
            continue

        if(lst[n_row][n_col] in now_visited):
            continue


        now_visited.append((n_row,n_col))
        used_direction[next_direction] = 1
        dfs(n_row,n_col,start_row,start_col,now_visited,used_direction,next_direction,num_desert+1)
        now_visited.pop()
        used_direction[next_direction] = 0


T = int(input())

for test_case in range(1,T+1):

    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]

    ans=0
    
    
    for row in range(N):
        for col in range(N):

            start_row = row
            start_col = col

            dfs(start_row,start_col,start_row,start_col,[lst[start_row][start_col]],[0,0,0,0],0,0)

    print(ans)
