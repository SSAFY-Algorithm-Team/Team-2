# 알고리즘 스터디 (삼성 SW 역량테스트 A.B형 대비)

> SSAFY 알고리즘 스터디 · 5인 · 날짜 유동

📖 **처음 오셨나요? → [깃허브 사용 가이드](GITHUB_GUIDE.md)**

---

## 📌 이번주 문제 (Week 02)

### 기본 문제

**DP**

| # | 문제 | 출처 | 난이도 | 유형 |
|:-:|---|---|:-:|---|
| 1 | [2 x n 타일링](https://school.programmers.co.kr/learn/courses/30/lessons/12900) | 프로그래머스 Lv.2 | 하 |  |
| 2 | [땅따먹기](https://school.programmers.co.kr/learn/courses/30/lessons/12913) | 프로그래머스 Lv.2 | 중하 |  |
| 3 | [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898) | 프로그래머스 Lv.3 | 중 |  |
| 4 | 햄버거 다이어트 (5215) | SWEA D3 | 중 |  |

> 💡 지난주 문제와 짝이 지어져 있습니다. `피보나치 수 → 2 x n 타일링`, `정수 삼각형 → 땅따먹기`, `요리사 → 햄버거 다이어트`

**DFS / BFS**

| # | 문제 | 출처 | 난이도 | 유형 |
|:-:|---|---|:-:|---|
| 5 | [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164) | 프로그래머스 Lv.3 | 중 | DFS 백트래킹 + 사전순 |
| 6 | 최장 경로 (2814) | SWEA D4 | 중 | DFS + 방문 복원 |
| 7 | [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163) | 프로그래머스 Lv.3 | 중 | BFS 최단 횟수 |
| 8 | 홈 방범 서비스 (2117) | SWEA D4 | 중 | BFS + 완전탐색 |

> 💡 번호 순서대로 푸시면 난이도가 완만하게 올라갑니다.

### 도전 문제 🔥

| 문제 | 출처 | 난이도 | 유형 |
|---|---|:-:|---|
| 보급로 (1249) | SWEA D4 | 중상 | 가중치 있는 최단경로 |

> 💡 일반 BFS로 풀면 틀립니다. 칸마다 이동 비용이 달라서 **다익스트라 / 0-1 BFS**가 필요해요.
> `heapq`는 B형에서 표준 무기이니 이번에 손에 붙여두시면 좋습니다.

--- 도전문제는 모든 팀에서 공유하는 문제입니다.
    다양한 풀이를 공유할 수 있도록 하겠습니다.

> ⚠️ SWEA 문제는 링크 대신 **번호**로 적어두었습니다. SWEA 사이트에서 번호로 검색해 주세요.

## 제출 방법 요약

```bash
git switch main
git pull
git switch -c {깃허브 닉네임}/{week-N}
# 문제 풀고 커밋
git push -u origin {깃허브 닉네임}/{week-N}
# GitHub에서 "Compare & pull request" 클릭
```

자세한 설명, 파일명 규칙, 오류 해결은 **[깃허브 사용 가이드](GITHUB_GUIDE.md)** 를 참고하세요.
