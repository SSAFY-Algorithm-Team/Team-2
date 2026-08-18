def solution(n, lost, reserve):
    
    answer=0
    
    lst=[1]*n
    for i in lost:
        lst[i-1]-=1
    for i in reserve:
        lst[i-1]+=1
    
    
    if(lst[0]==0 and lst[1]==2):
        lst[0]+=1
        lst[1]-=1
    
    for i in range(1,n-1):
            
        if(lst[i]==0):
            if(lst[i-1]==2):
                lst[i-1]-=1
                lst[i]+=1
                continue
            elif(lst[i+1]==2):
                lst[i+1]-=1
                lst[i]+=1
    
    if(lst[n-1]==0 and lst[n-2]==2):
        lst[n-1]+=1
        lst[n-2]-=1
    
    for i in lst:
        if(i>=1):
            answer+=1
                    
    return answer