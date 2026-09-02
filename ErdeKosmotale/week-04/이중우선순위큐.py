import heapq
from collections import defaultdict

def solution(operations):

    heap_max=[]
    heap_min=[]
    
    dict_check=defaultdict(int)
    
    size=0
    
    answer=[]
    
    for cmd in operations:
        
        cmd_first, num = cmd.split()
        num = int(num)
        
        if(cmd_first=='I'):
            heapq.heappush(heap_max,-num)
            heapq.heappush(heap_min,num)
            
            dict_check[num]+=1
            size+=1
            
        else:
            if(size==0):
                continue
            
            if(num==1):        #최댓값 삭제 확인
                
                while(dict_check[-heap_max[0]]==0):
                    heapq.heappop(heap_max)
                    
                dict_check[-heap_max[0]]-=1
                heapq.heappop(heap_max)
                
                
            else: #최솟값 삭제
                while(dict_check[heap_min[0]]==0):              
                    heapq.heappop(heap_min)
                
                dict_check[heap_min[0]]-=1
                heapq.heappop(heap_min)
                
            
            size-=1
    
    if(size==0):
        return [0,0]
    
    while(dict_check[-heap_max[0]]==0):
        heapq.heappop(heap_max)
    
    while(dict_check[heap_min[0]]==0):
        heapq.heappop(heap_min)
        
    return [-heap_max[0],heap_min[0]]
    
        
    
    

        