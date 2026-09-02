# 0번째 원소가 k이상이면 종료
# heapq을 사용해서 최소화 시킴

# 0번째 원소가 k보다 작으면 섞어야 함.
# 섞고 힙에 다시 넣기


import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    now_spicy=0
    print(scoville)
    answer=0
    while(scoville):
        
        if(scoville[0]>=K):
            break
        
        answer+=1
        
        if(now_spicy>=K):
            now_spicy=0
            continue
        
        if(now_spicy==0):
            now_spicy=heapq.heappop(scoville)
        
        else:
            now_spicy+= 2*(heapq.heappop(scoville))
        
        
        
    return answer