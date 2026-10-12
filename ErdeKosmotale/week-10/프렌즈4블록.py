from collections import deque

def check2(lst,row,col):
    
    direction = [(0,1),(1,0),(1,1)]
    
    if(lst[row][col]=='0'):
        return False
    
    for r,c in direction:
        
        n_row = row + r
        n_col = col + c
        
        if(lst[row][col]!=lst[n_row][n_col]):
            return False
        
    return True


def make_down(lst,m,col):
    
    stack=[]
    
    for row in range(m):
        
        if(lst[row][col]!='0'):
            stack.append(lst[row][col])
            lst[row][col] = '0'    
    
    k= m-1
    
    while(stack):
        
        s= stack.pop()
        lst[k][col] = s
        k= k-1
        
    return
        
        
        
    


    
def solution(m, n, board):
    
    board_t = []
    
    for k in board:
        board_t.append(list(k))
    
    def find():
        
        while(True):
            
            lst_delete= []
            
            for row in range(m-1):
                for col in range(n-1):
                    if(check2(board_t,row,col)):
                        lst_delete.append((row,col))
                        lst_delete.append((row,col+1))
                        lst_delete.append((row+1,col))
                        lst_delete.append((row+1,col+1))
                          
            if(not lst_delete):
                break
                
            
                
            set_delete = set()
            
            for r, c in lst_delete:
                board_t[r][c]= '0'
                set_delete.add(c) 
                
            for c in set_delete:
                make_down(board_t,m,c)
            
              
    find()
    
    
    answer = 0
    
    for r in range(m):
        for c in range(n):
            if(board_t[r][c]=='0'):
                answer+=1
    return answer