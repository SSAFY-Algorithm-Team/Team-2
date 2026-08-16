#구명보트, 프로그래머스, 
#소요시간: 40분
#하드코딩 하다가 시간초과, 다른 접근법 사용

def solution(people, limit):
    
    people=sorted(people)
    num_people=len(people)
    num_saved=0
    num_vote=0
    
    right=num_people-1
    left=0
    
    while(True):
        
        if(left>right):
            break
        
        sum_weight=people[right]+people[left]
        
        if(sum_weight<=limit):
            right-=1
            left+=1
            num_saved+=2
            num_vote+=1
        else:
            right-=1
            num_vote+=1
        
        
    
    return num_vote








# 시간초과 풀이 1

# def solution(people, limit):
    
#     people=sorted(people)
#     num_vote=0
#     num_saved=0
    
#     num_people=len(people)
#     turn=num_people-1 #구해지는 사람!
#     saved=[False]*num_people
    
#     while(num_saved<num_people):
        
#         flag=False #두 명 구할수 있을때 flag가 True
        
#         if(saved[turn]==True):
#             turn-=1
#             continue
        
#         if(num_saved==num_people-1):
#             num_saved+=1
#             num_vote+=1
#             saved[turn]=True
#             break
        
#         for i in range(turn-1,-1,-1):
#             if(saved[i]):
#                 continue
                
#             if(people[turn]+people[i]<=limit):
#                 saved[turn]=True
#                 saved[i]=True
#                 num_vote+=1
#                 num_saved+=2
#                 flag=True
#                 break
    
#         if(flag==True):
#             turn-=1
#             continue
#         else:
#             saved[turn]=True
#             num_vote+=1
#             num_saved+=1
#             turn-=1
        
#     return num_vote