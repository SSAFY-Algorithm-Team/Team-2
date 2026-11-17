
def find(x):

    if parent[x] !=x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a,b):

    a = find(a)
    b = find(b)

    if a!=b:

        parent[b] = a

T = int(input())

for test_case in range( 1 , T + 1):

    n,m = map(int,input().split())

    parent = [0] * (n+1)

    ans = ''

    for i in range(1,n+1):
        parent[i] = i

    for i in range(m):

        cmd, start, end = map(int,input().split())

        if(cmd == 0):

            union(start,end)
            
        else:

            if(find(start) == find(end)):
                ans += '1'

            else:
                ans += '0'

    print(f"#{test_case} {ans}")
            
