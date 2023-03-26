#BOJ1388_바닥장식4_S4
#https://www.acmicpc.net/problem/1388   

# 일반 2차원 배열의 확인으로도 풀 수 있고
# dfs로도 풀 수 있을 것 같다. 

n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(input()))

cnt = 0
#판자 나무 개수를 구하고, -나 |를 만날때마다 cnt를 더해준다
for i in range(n):
    go = ''
    for j in range(m):
        if room[i][j] == '-':
            if room[i][j] != go:
                cnt += 1
        go = room[i][j]


for j in range(m):
    go = ''
    for i in range(n):
        if room[i][j] == '|':
            if room[i][j] != go:
                cnt += 1
        go = room[i][j]

print(cnt)

# dfs 알고리즘 함수 정의
def dfs(x,y):
    # 바닥 장식 모양이 '-' 일 때
    if graph[x][y] == '-':
        graph[x][y] = 1	    # 해당 노드 방문처리
        for _y in [1,-1]:   # 양옆(좌우) 확인하기
            Y = y + _y
            # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x,Y)
    # 바닥 장식 모양이 '|' 일 때
    if graph[x][y] == '|':
        graph[x][y] = 1	    # 해당 노드 방문처리
        for _x in [1,-1]:   # 상하(위아래) 확인하기
            X = x + _x  
            # 상하 노드가 주어진 범위를 벗어나지 않고 '|' 모양이라면 재귀함수 호출
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X,y)
 
n,m = map(int, input().split()) # 방 바닥의 세로 크기 n, 가로 크기 m
graph = []  # 2차원 리스트의 맵 정보 저장할 공간
for _ in range(n):
    graph.append(list(input()))
 
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i,j)    # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
            count += 1
 
print(count)