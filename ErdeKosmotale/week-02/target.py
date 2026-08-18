#프로그래머스, 타겟넘버
#풀이시간: 약 15분

def product(lst,r):
    
    path=[]
    result=[]
    
    def backtrack():
        
        for i in range(len(lst)):
            
            if(len(path)==r):
                result.append(path[:])
                return
            
            path.append(lst[i])
            backtrack()
            path.pop()
            
    backtrack()
    return result


def solution(numbers, target):
    
    n_numbers=len(numbers)

    answer = 0
    
    lst_products=product(['+','-'],n_numbers)
    
    for lst_product in lst_products:
        sum_product=0
        for i in range(n_numbers):
            if(lst_product[i]=='+'):
                sum_product+=numbers[i]
            else:
                sum_product+= (-1*numbers[i])
        
        if(sum_product==target):
            answer+=1
    
    
    
    return answer