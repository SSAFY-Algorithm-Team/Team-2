

def is_promising(x):

    for i in range(x): #x는 현재 탐색하는 row
                       #i는
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False

    return True

def n_queens(x):

    global ans

    if x == n:
        ans += 1
        return

    else:
    
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

T= int(input())

for test_case in range(1,T+1):

    n = int(input())

    ans = 0
    row = [0] * n    


    n_queens(0)


    print(f"#{test_case} {ans}")






































# def check(row,col):

#     #좌상 대각 우상 대각
#     #좌하 대각 우하 대각
#     # 같은 열 확인

#     if(sum[lst[row]]>=2):
#         return False

#     # 같은 행 확인

#     for r in range(N):
#         if(lst[r][col]):
#             return False

#     # 대각선 오른쪽 위

#     a = row - 1
#     b = col + 1

#     while(0<= a < N and 0<= b < N):
#         if(lst[a][b]):
#             return False
#         a-=1
#         b+=1

#     a = row + 1
#     b = col + 1

#     while(0<= a < N and 0<= b < N):
#         if(lst[a][b]):
#             return False

#         a+=1
#         b+=1

#     a= row - 1
#     b= col - 1

#     while(0<= a < N and 0 <= b < N):
#         if(lst[a][b]):
#             return False

#         a-=1
#         b-=1

#     a= row + 1
#     b= col - 1

#     while(0<= a < N and 0 <= b < N):
#         if(lst[a][b]):
#             return False

#         a+=1
#         b-=1  
            
#     return True


# def dfs(k,r,c):

#     global ans
#     if(k==N):
#         if(check(r,c)):

#     for row in range(N):
#         for col in range(N):
#             if(check(row,col)):
#                 dfs(k+1,r,c)
                
            
            


# T = int(input())

# for test_case in range(1,T+1):

#     N=int(input())

#     lst=[[0]*N for _ in range(N)]

#     ans = 0
    

        