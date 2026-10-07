# programmers 이모티콘 할인행사
# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 시간 2: 40~


"""
문제 요약
1. 가입자 최대
2. 판매액 최대


n명의 사용자에게 이모티콘 m개 할인 판매
할인률 10 20 30 40 중 1

각 사용자는 자신의 기준에 따라 일정 비율 이상 할인 이모티콘 모두 구매
각 사용자는 자신의 기준에 따라 구매 비용 합이 일정 이상이 된다면, 이모티콘 구매를 모두 취소하고 플러스 서비스 가입

입력 : [[할인 기준, 플러스 구매 기준], ..] // [임티가격1, 임티가격2, ...]
출력 : 행사 목적을 최대한으로 달성했을 때 [이모티콘 플러스 서비스 가입 수, 매출액]
"""


RATE = [40, 30, 20, 10] # 할인률

def solution(users, emoticons):

    best_amount = best_cnt = 0
    amount = [0] * len(users)

    def dfs(depth):
        nonlocal best_amount, best_cnt

        if depth == len(emoticons):

            # 가입한 사람 세기
            is_cnt = [False] * len(users)
            for i in range(len(users)):
                if amount[i] >= users[i][1]:
                    is_cnt[i] = True

            # is_cnt가 False인 금액만 더하기
            curr_amount = 0
            for i in range(len(is_cnt)):
                if not is_cnt[i]:
                    curr_amount += amount[i]

            cnt = sum(is_cnt)

            # cnt가 best_cnt보다 크면 best_cnt, best_amount 업뎃
            if cnt > best_cnt:
                best_cnt = cnt
                best_amount = curr_amount
            # cnt가 best_cnt와 같고, user_amount가 더 크면 업뎃
            elif cnt == best_cnt:
                best_amount = max(best_amount, curr_amount)
            return


        # 할인률 4개 적용해보기
        for i in range(4):
            # print(depth, i)
            
            # emoticons[depth] * rate[i] ==> 할인률 적용
            discounted = emoticons[depth] * (100 - RATE[i]) // 100
            print(discounted)
            # print(discounted, RATE[i])
            
            # users돌며 rate[i]보다 낮은 할인율이면 구매 -> amount[idx]에 저장
            # amount에서 users[idx]][1]보다 높은 값 매치되면 -> cnt = 1로 is_cnt[인덱스] = True로 변환
            for idx, [rate, _] in enumerate(users):
                if rate <= RATE[i]:
                    amount[idx] += discounted
                    # if amount[idx] >= price:
                    #     is_cnt[idx] = True

            dfs(depth + 1)

            # 다시 빠져나올때
            for idx, [rate, _] in enumerate(users):
                if rate <= RATE[i]:
                    amount[idx] -= discounted
                    # if amount[idx] >= price:
                    #     is_cnt[idx] = False
    
    dfs(0)

    answer = [best_cnt, best_amount]
    return answer


ans = solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
print(ans)