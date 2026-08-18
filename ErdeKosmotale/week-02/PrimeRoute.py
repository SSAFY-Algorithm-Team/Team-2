import sys
sys.stdin = open("input.txt", "r")

ans=10**9
def permutation(dots,r,dots_ent,dots_home):

    global ans
    path=[]
    used=[False]*len(dots)


    def backtrack():
        global ans
        
        if(len(path)==r):

            ans_inter=0
            ans_inter+= abs(dots[path[0]][0]-dots_ent[0])
            ans_inter+= abs(dots[path[0]][1]-dots_ent[1])
            ans_inter+= abs(dots[path[-1]][0]-dots_home[0])
            ans_inter+= abs(dots[path[-1]][1]-dots_home[1])
            x_sum=0
            y_sum=0

            for i in range(1,len(path)):

                x_sum = abs(dots[path[i]][0]-dots[path[i-1]][0])
                y_sum = abs(dots[path[i]][1]-dots[path[i-1]][1])
                
                ans_inter+= (x_sum+y_sum)
                if(ans_inter>=ans):
                    return
            
            ans=min(ans,ans_inter)
            return
        
        for i in range(len(dots)):
            if(used[i]==False):
                used[i]=True
                path.append(i)
                backtrack()
                used[i]=False
                path.pop()

    backtrack()

    return
              
            
T = int(input())

# 집 크기는 100X100입니다.

for test_case in range(1, T + 1):

    ans=10**9

    n_customer=int(input())

    lst=list(map(int,input().split()))

    dots=[]
    for i in range(4,len(lst),2):
        dots.append((lst[i],lst[i+1]))

    dots_ent=(lst[0],lst[1])
    dots_home=(lst[2],lst[3])

    permutation(dots,n_customer,dots_ent,dots_home)
    
    print(f"#{test_case} {ans}")
    