# N이 10만이라 .. 원래 하려던 방식은 2중for문 돌면 불가능 ㅠㅠ
# 혼자서 코드 완성하고싶다..
from bisect import bisect_left

# 모든 경우에 해당하는 score를 저장하는 함수
def make_keys(data, score, db):
    def dfs(idx, key):
        if idx == 4:
            key_str = ' '.join(key)

            if key_str not in db:
                db[key_str] = []

            db[key_str].append(score)
            return

        # 원래 값 사용
        dfs(idx + 1, key + [data[idx]])

        # - 사용
        dfs(idx + 1, key + ['-'])

    dfs(0, [])

def solution(info, query):
    db = {}

    # info 전처리
    for person in info:
        data = person.split()

        score = int(data[4])
        conditions = data[:4]

        make_keys(conditions, score, db)

    # 각 조건별 점수 정렬
    for key in db:
        db[key].sort()

    answer = []

    # query 처리
    for q in query:
        q = q.replace(' and ', ' ')
        data = q.split()

        conditions = data[:4]
        target_score = int(data[4])

        key = ' '.join(conditions)
        
        # info 조건에 없는 경우
        if key not in db:
            answer.append(0)
            continue

        scores = db[key]

        idx = bisect_left(scores, target_score)

        answer.append(len(scores) - idx)

    return answer