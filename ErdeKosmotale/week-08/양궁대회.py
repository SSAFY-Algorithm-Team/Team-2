#가지치기를 어떻게...

def solution(n, info):
    answer = []
    
    # 중복 순열 문제인듯.     
    
    def product():
        
        path= [0] * 11
        best_gap = -1
        best_path = []
        
        def backtrack(idx,start):
            
            nonlocal best_gap
            nonlocal best_path
            
            if(idx==n):

                score_apache = 0
                score_lion   = 0
                
                for i in range(11):
                    if(info[i]==0 and path[i]==0):
                        continue
                    if(info[i] >= path[i]):
                        score_apache += (10-i)
                    else:
                        score_lion += (10-i)
                
                if(score_lion > score_apache):
                    now_gap = score_lion - score_apache
                    
                    if(now_gap > best_gap):
                        best_path = path[:]
                        best_gap  = now_gap
                        
                    elif(now_gap == best_gap):
                        
                        for i in range(10,-1,-1):
                            if(path[i] > best_path[i]):
                                best_path = path[:]
                                break
                            elif(path[i]==best_path[i]):
                                continue
                                
                            else:
                                break
                                
                                  
                return
                            
            for i in range(start,11):
                path[i]+=1
                
                if(info[i]>=path[i]):
                    backtrack(idx+1,i)
                
                else:
                    backtrack(idx+1,i+1)
                
                path[i] -= 1
                    
        backtrack(0,0)
    
        return best_path

    result = product()
    
    if result==[]:
        result=[-1]
        
    return result