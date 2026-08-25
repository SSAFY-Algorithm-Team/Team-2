
#프로그래머스 여행경로

#완전한 백트래킹 문제였습니다.

#dfs 결과가 None으로 반환될 때를 처리해야 함


import sys
sys.setrecursionlimit(10**9)

def dfs(lst,path_t,idx):
    
    result=[]
    
    path=[["",""]]
    path[0][0]=path_t[0]
    path[0][1]=path_t[1]
    
    
    n=len(lst)
    used=[False]*n
    used[idx]=True
    
    def backtrack():
        
        if(len(path)==n):
            
            result_inter=[]
            for i in range(n):
                result_inter.append(path[i][0])
            result_inter.append(path[n-1][-1])
            result.append(result_inter[:])
            return
        
        for i in range(n):
             
            if(i==idx):
                continue
            
            if(path[-1][1]==lst[i][0] and used[i]==False):
                
                path.append(lst[i])
                used[i]=True
                backtrack()
                used[i]=False
                path.pop()
            
    backtrack()
    
    return result
###########################################
def find_min_str(result):
    
    idx=0
    str_now='ZZZZZZZZZZZ'
    
    for i in range(len(result)):
        
        t=''.join(result[i])
        
        if(t<str_now):
            str_now=t
            idx=i
            
    return str_now,result[idx]
#################################################

def solution(tickets):
    path=[]
    lst_idx=[]
    
    for i in range(len(tickets)):
        if(tickets[i][0]=="ICN"):
            path.append(tickets[i])
            lst_idx.append(i)
    
    str_ans='ZZZZZ'
    result_now=[]
    for k in range(len(path)):
        
        ans_lst=dfs(tickets,path[k],lst_idx[k])
        
        if(not ans_lst):  #이게 진짜 폭력적임
            continue
        str_now,result_now=find_min_str(ans_lst)
        
        if(str_ans>str_now):
            result=result_now
            str_ans=str_now
    return result