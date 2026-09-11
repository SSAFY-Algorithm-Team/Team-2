T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result_number = 0
    result_count =  0
    N = int(input())
    arr = list(map(int,input()))
    arr_dic = {}
    for i in arr:
        arr_dic[i] = arr_dic.get(i,0) + 1
    print(arr_dic)
    max = -1
    for key,value in arr_dic.items():
        if value > max:
            result_number = key
            max = value
        elif value == max and result_number < key:
            result_number = key
    print(f"#{test_case} {result_number} {max}")