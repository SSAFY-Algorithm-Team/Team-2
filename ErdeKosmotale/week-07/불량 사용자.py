# 응모 id
# ban id


def check_id(banned_id,user_id):           # 지금 체크하는 부분이 밴 id랑 같은지 확인
    
    if(len(banned_id)!=len(user_id)):
        return False
    
    for i in range(len(banned_id)):
        if(banned_id[i]=='*'):
            continue
        
        if(banned_id[i]!=user_id[i]):
            return False
    
    return True
    
    
def solution(user_id, banned_id):
    
    answer = set()
    
    #banned_id에서
    
    sub_lst=[[] for _ in range(len(banned_id))]
    
    for user in user_id:
        for i in range(len(banned_id)):
            
            if(check_id(banned_id[i],user)):
                sub_lst[i].append(user)
    
    
    
    def dfs(idx,ban_lst_answer):
        nonlocal answer
        if(len(ban_lst_answer)==len(banned_id)):
            
            ban_lst_answer=sorted(ban_lst_answer)
            answer.add(''.join(ban_lst_answer))
            return
        
        for i in sub_lst[idx]:
            if(i not in ban_lst_answer):
                ban_lst_copy = ban_lst_answer[:]
                ban_lst_copy.append(i)
                dfs(idx+1,ban_lst_copy)
                
    dfs(0,[])
                
            
    print(answer)
    
    
    
    
    return (len(answer))