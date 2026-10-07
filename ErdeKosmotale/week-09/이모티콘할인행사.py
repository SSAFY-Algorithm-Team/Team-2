def combination_full(users,emoticons):
    
    path = []
    len_emoticons = len(emoticons)
    
    user_plus = 0
    user_buying_price = 0
    
    def dfs():
        
        nonlocal user_plus
        nonlocal user_buying_price
        
        lst  = [10, 20, 30, 40]
        
        if(len(path) == len_emoticons):           #path의 각 원소의 값은
            
            user_buying = [0] * len(users)
            user_plus_now = 0
            user_buying_now  = 0
            
            for i in range(len(users)):
            
                user = users[i]

                user_discount = user[0]
                user_limit    = user[1]
                
                for j in range(len_emoticons):
                    price = emoticons[j]
                    now_discount = path[j]
                    if(now_discount>=user_discount):
                        user_buying[i] += int(price*(100-now_discount)/100)
                        
                        if(user_buying[i]>=user_limit):
                            user_buying[i]= -1
                            break
            
            for t in user_buying:  
                
                if(t==-1):
                    user_plus_now += 1
                else:
                    user_buying_now += t
            
            if(user_plus<user_plus_now):
                user_plus = user_plus_now
                user_buying_price = user_buying_now
            
            elif(user_plus == user_plus_now):
                if(user_buying_now>user_buying_price):
                    user_buying_price = user_buying_now
            
            return
        
        for i in range(4):
            path.append(lst[i])
            dfs()
            path.pop()
    
    dfs()
    
    return user_plus, user_buying_price


def solution(users, emoticons):
    
    ans1,ans2 =combination_full(users,emoticons)
    
    return [ans1,ans2]


