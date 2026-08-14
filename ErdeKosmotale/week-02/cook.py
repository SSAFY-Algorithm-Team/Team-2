#SWEA 4012. 요리사
#소요시간: 40분 / 시도 1회

def combination(lst,r):


    path=[]
    result=[]
    
    def backtrack(start):
        for i in range(start,len(lst)):

            if(len(path)==r):
                other=[]
                for j in range(len(lst)):
                    if(j not in path):
                        other.append(j)

                result.append((path[:],other[:]))
                return
      
            path.append(i)
            backtrack(i+1)
            path.pop()
                
    backtrack(0)

    return result

def find_sum(lst):

    sum=0

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            sum+=lst[i][j]

    return sum

T = int(input())

for test_case in range(1, T + 1):
        
    n=int(input())

    lst=[list(map(int,input().split())) for _ in range(n)]

    sum_cook=find_sum(lst)
    ans=10**9

    len_combi=len(lst)//2
    combi=combination(lst,len_combi)

    for com, com2 in combi:
        ans_inter=0
        ans_inter2=0
        for i in range(len_combi-1):
            for j in range(i+1,len_combi):
                x=com[i]
                y=com[j]
                ans_inter+=lst[x][y]
                ans_inter+=lst[y][x]

                x1=com2[i]
                y1=com2[j]
                ans_inter2+=lst[x1][y1]
                ans_inter2+=lst[y1][x1]

                # print(com,com2)
                # print(ans_inter, ans_inter2)
        ans_in=abs(ans_inter-ans_inter2)

        #A=ans_inter, B= sum-ans_inter
        
        ans=min(ans,ans_in)
    
    print(f"#{test_case} {ans}")