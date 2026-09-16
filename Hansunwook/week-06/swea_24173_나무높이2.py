
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 일단 먼저 트리가 맥스값까지 가야할 오차를 각각 구하고
# 배열로 만든다 
# 예를 들어 첫번쨰 케이스에서 오차가 2,8이니깐.....
# 2는 그대로 놓고 8을 쪼개는식으로........?
# 결국 1,2,3 이 반복되어서 더해지고 이걸 조합해서 뭘 만드는건데,,,
# 그래서 조합했을 경우에 제일 안겹치고 1,2,3 펼쳐지면 제일 좋은 것?
# 만약 작은 숫자인 2를 먼저 넣고 그 후에 넣는다면 어떻게 보장하지
# 그러면 최대한 3으로 잘라볼까
# 왜냐하면 1,2로 3 만들 수 있기 때문....
# 이렇게 해서 1개수 세서 그냥 1-- 1-- 1 이런식으로 7개임
# 그래서 규칙을 보자면 지난 시간 3으로 나눴을 때 나머지 0,1,2
#  ->  0: 그냥 시작, 1: 2 더하고 시작, 2: 1 더하고 시작
# 2개수는 1개수에서 일단 뺀 다음 12- 12- 1 여기서 그 나머지 남으면 
# 그때부터 12- 12- 12- 이렇게면 처음 1 제외 4개나옴
# 그래서 규칙을 보자면 지난 시간 3으로 나눴을 때 나머지 0,1,2
#  ->  0: 1 더하고 시작, 1: 그냥 시작, 2: 2 더하고 시작
# 2에 하나 더해짐
# 그리고 1 더해지는것도 4에 하나라 신경써야함
# 마지막으로 그냥 3은 시작을 0으로 한다면 2에 하나, 3에 두개
# 그래서 
#이게맞ㅇ나
for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    tree = list(map(int,input().split()))
    max_tree = max(tree)
    tree_ups = []
    for i in tree:
        a = max_tree-i
        if a == 0:
            continue
        tree_ups.append(a)
    count1=0
    count2=0
    count3=0
    tree_nums = []
    for tree_up in tree_ups:
        n = tree_up
        if tree_up==1:
            print("그냥 1임")
            count1 += n
            continue
        print("###############3,2,1 비율 추가하는중..",tree_up)
        count3 += n//3
        n = n%3 
        print("3의 개수는: ",count3)
        print("이제 다음 오차: ",n)
        count2 += n//2
        n = n%2
        print("2의 개수는: ",count3)
        print("이제 다음 오차: ",n)
        count1 += n
        print("1의 개수는: ",n)
        tree_nums.append
    print("최종 각자의 3,2,1 개수: ",count3,"x3",count2,"x2",count1,"x1")


    print(f"#{test_case} {result}")