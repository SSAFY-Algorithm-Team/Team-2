T=int(input())

def factorial(n):

    if(n==0 or n==1):
        return 1

    lst= [1]*(n+1)

    for i in range(2,n+1):
        lst[i]=lst[i-1]*i

    return lst[n]

def permutation(n,r): 

    return factorial(n) / (factorial(n-r+1))    

def combination(n,r):

    global ans

    path = []
    used= [0] * (n+1)

    def backtrack(start):

        global ans

        if(len(path)==r):

            sum_path= sum(path)

            if(2*sum_path >= sum_lst):
                ans+=permutation(n,r)

            return
        
        for i in range(start,N):

            path.append(lst[i])
            backtrack(i+1)
            path.pop()

    backtrack(0)


for test_case in range(1,T+1):

    N = int(input())

    lst= list(map(int,input().split()))

    ans=0    

    sum_lst=sum(lst)

    for i in range(1,N+1):
        combination(N,i)


    print(f"#{test_case} {ans}")