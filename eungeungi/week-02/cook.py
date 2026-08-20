def cal(N, arr):
    ans = float('inf')  # 지금까지 찾은 최소 맛 차이 (처음엔 무한대로 시작)

    def score(li):
        # li(그룹 안 식재료 인덱스들)의 맛(시너지 총합)을 계산하는 함수
        answer = 0
        for i in li:
            for j in li:
                if i != j:  # 자기 자신과의 쌍은 제외
                    answer += arr[i][j]  # i를 j와 요리했을 때의 시너지 더하기
        return answer

    def backtrack(idx, a):
        # idx: 지금부터 A그룹에 넣을지 말지 판단할 식재료 번호
        # a: 지금까지 A그룹으로 확정한 식재료 인덱스 리스트
        nonlocal ans  # cal 함수의 ans 변수를 직접 수정하겠다는 선언

        # [종료 조건] A그룹이 목표 개수(N/2)만큼 다 채워졌을 때
        if len(a) == N // 2:
            # A그룹에 없는 나머지 인덱스들이 자동으로 B그룹이 됨
            b = [i for i in range(N) if i not in a]
            score_a = score(a)          # A음식의 맛 계산
            score_b = score(b)          # B음식의 맛 계산
            ans = min(ans, abs(score_a - score_b))  # 지금까지의 최솟값과 비교해서 갱신
            return  # 이 경로는 다 끝났으니 재귀 종료

        # [가지치기] 남은 재료로는 A그룹을 절대 다 못 채우는 경우 미리 차단
        # N - idx        : 아직 결정 안 한(남은) 식재료 개수
        # N//2 - len(a)  : A그룹을 완성하려면 앞으로 더 넣어야 할 개수
        if N - idx < N // 2 - len(a):
            return  # 못 채우는 게 확정이므로 더 진행할 필요 없음
            # (이 가지치기가 없으면 idx가 N을 넘어서까지 진행되어
            #  arr[N] 같은 존재하지 않는 인덱스를 참조하게 되어 오류 발생)

        # [갈래 1] idx번 식재료를 A그룹에 "넣는" 경우
        a.append(idx)
        backtrack(idx + 1, a)
        a.pop()  # 다음 갈래에 영향 주지 않도록 원상복구 (백트래킹 핵심)

        # [갈래 2] idx번 식재료를 A그룹에 "안 넣는" 경우 (B그룹행)
        backtrack(idx + 1, a)

    # 0번 식재료는 무조건 A그룹으로 고정하고 시작
    # (A/B 이름표만 바뀐 대칭적인 중복 탐색을 절반으로 줄이기 위함)
    backtrack(1, [0])

    return ans  # 모든 경로를 다 탐색한 뒤의 최소 맛 차이 반환


# ----- 입력 처리 및 실행 -----
T = int(input())  # 테스트케이스 개수
for tc in range(1, T + 1):
    N = int(input())  # 이번 테스트케이스의 식재료 개수
    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)  # N x N 시너지 표 읽어오기

    ans = cal(N, arr)  # 이번 테스트케이스의 정답 계산
    print(f"#{tc} {ans}")  # 형식에 맞춰 출력