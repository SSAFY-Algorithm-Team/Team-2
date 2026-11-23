import sys
input = sys.stdin.readline

def find(x):

    if(x!=parent[x]):
        parent[x] = find(parent[x])

    return parent[x]

def union(x,y):

    x_u = find(x)
    y_u = find(y)

    if(x_u != y_u):
        parent[y_u] = x_u 
        
N = int(input())
M = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
lst_cmd = list(map(int,input().split()))

parent = list(range(N)) 

for i in range(N):
    for j in range(N):
        if(lst[i][j]==1):
            union(i,j)

ans = 'YES'

t= find(lst_cmd[0]-1)

for i in range(1,len(lst_cmd)):

    num_cmd = lst_cmd[i]
    num_cmd -= 1

    find_now = find(num_cmd)

    if(t!= find_now):
        ans = 'NO'
        break

    t = find_now

print(ans)

    

