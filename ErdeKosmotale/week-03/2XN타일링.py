#프로그래머스 2xn 타일링

#점화식을 잘 세우면 어렵지 않음. 결과는 피보나치 수열임.


def solution(n):
    
    if(n==1):
        return 1
    
    if(n==2):
        return 2
    
    lst=[0]*(n+1)
    lst[1]=1
    lst[2]=2
    
    
    
    for i in range(3,n+1):
        lst[i]= (lst[i-2]+lst[i-1])%1000000007
    
    answer=lst[n]  
    
    return answer