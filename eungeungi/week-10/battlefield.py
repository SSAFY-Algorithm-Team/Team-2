# inp에 있는 값을 하나씩 빼면서
# s인 경우 범위 벗어나지 않을 때 까지 *이나 #을 만나는지 
# 만난다면 *이면 .으로 바꾸고 break #을 만나면 break
# U,D,L,R인 경우 각 방향의 다음칸이 .이면 이동 아니면 현재값 U,D,L,R에 맞는 화살표 표시로 마무리


def battle(H,W,arr,inp,start):
    x,y = start
    # 방향 설정
    if arr[x][y] == '>':
        dir = (0,1)
    elif arr[x][y] =='<':
        dir = (0,-1)
    elif arr[x][y] == '^':
        dir = (-1,0)
    else:
        dir = (1,0)
    
    for i in inp:
        if i == 'S':
            nx, ny = x+dir[0], y+dir[1]
            while 0<= nx < H and 0<= ny < W:
                if arr[nx][ny] == '#':
                    break
                elif arr[nx][ny] == '*':
                    arr[nx][ny] = '.'
                    break
                nx += dir[0]
                ny += dir[1]

        elif i == 'U':
            dir = (-1,0)
            arr[x][y] = '^'
            nx, ny = x-1,y
            if (0<= nx < H and 0<= ny < W) and arr[nx][ny] == '.':
                arr[x][y] = '.'
                x,y = nx,ny
                arr[x][y] = '^'
        
        elif i == 'D':
            dir = (1,0)
            arr[x][y] = 'v'
            nx, ny = x+1,y
            if (0<= nx < H and 0<= ny < W) and arr[nx][ny] == '.':
                arr[x][y] = '.'
                x,y = nx,ny
                arr[x][y] = 'v'

        elif i == 'R':
            dir = (0,1)
            arr[x][y] = '>'
            nx, ny = x,y+1
            if (0<= nx < H and 0<= ny < W) and arr[nx][ny] == '.':
                arr[x][y] = '.'
                x,y = nx,ny
                arr[x][y] = '>'
        
        else:
            dir = (0,-1)
            arr[x][y] = '<'
            nx, ny = x,y-1
            if (0<= nx < H and 0<= ny < W) and arr[nx][ny] == '.':
                arr[x][y] = '.'
                x,y = nx,ny
                arr[x][y] = '<'
    return arr



T = int(input())
for tc in range(1,T+1):
    H, W = map(int, input().split())
    arr = []
    for i in range(H):
        row = list(input())
        arr.append(row)
        for j in range(W):
            if row[j] in ['>', '<', '^', 'v']:
                start = (i,j)
    N = int(input())
    inp = input().strip()
    ans = battle(H,W,arr,inp,start)
    print(f"#{tc} ", end ='')
    for row in ans:
        print(''.join(row))