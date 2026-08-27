from collections import defaultdict
def solution(tickets):
    kind = defaultdict(list)
    # defaultdict가 없으면 {} 설정
    for start, end in tickets:
        # if start not in kind:
        #   kind[start] = []
        kind[start].append(end)
    # 나중에 pop해서 쉽게 빼내기 위해 거꾸로 설정
    for start in kind:
        kind[start].sort(reverse=True)
    result = []
    def dfs(air):
        # while air in kind and kind[air]:
        # 일반 딕셔너리로 설정하면 air가 key에 없는 경우도 있음
        # defaultlist를 사용하면 빈 리스트를 자동으로 만들어줘서
        # air in kind를 굳이 확인하지 않아도 됨
        while kind[air]:
            nxt = kind[air].pop()
            dfs(nxt)
        result.append(air)
    dfs("ICN")
    return result[::-1]