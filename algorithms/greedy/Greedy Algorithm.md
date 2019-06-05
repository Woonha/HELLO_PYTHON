# Greedy Algorithm

###### 탐욕 알고리즘, 욕심쟁이 알고리즘

: 미래를 고려하지 않고 각 단계에서 최선을 선택하는 알고리즘

- 동적 프로그래밍과 같이 최적화 문제를 푸는 데 사용
- 동적 프로그래밍과 함께 쓰이며 서로 보완하는 개념
- 항상 최적의 해를 보장하지는 않음



###### 알고리즘

1. 해 선택 (Selection Procedure) : 지금 당시에 가장 최적인 해를 구한 뒤, 이를 부분해 집합에 추가한다.
2. 적절성 검사 (Feasibility Check) : 새로운 부분해 집합이 적절한지 검사한다.
3. 해 검사 (Solution Check) : 새로운 부분해 집합이 문제의 해가 되는지 검사한다. 아직 문제의 해가 완성되지 않았다면 1번부터 다시 시작한다.



###### 예

- 거스름돈 나누기
- Prim Algorithm, Kruskal Algorithm : Minimum Spanning Tree를 구하는 방법
- Dijkstra Algorithm : 가중치가 있는 방향 그래프에서 최단 거리를 구하는 방법

