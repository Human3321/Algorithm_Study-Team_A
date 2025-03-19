'''
    n은 세로, m은 가로
    1. I를 탐색
    2. 이동한 곳은 X로 변경
    3. bfs 또는 dfs 를 사용
    4. P를 만나면 count++
'''

import sys
from collections import deque

def bfs(road,start,n,m):
    q = deque([start])
    ab = [[0,1],[0,-1],[1,0],[-1,0]]
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in ab:
            x_,y_ = x+i[0],y+i[1]
            if x_ <= -1 or x_>=n or y_ <=-1 or y_>=m:
                continue
            if road[x_][y_] == 'O':
                road[x_][y_] = 'X'
                q.append([x_,y_])
            elif road[x_][y_] == 'P':
                road[x_][y_] = 'X'
                q.append([x_,y_])
                cnt += 1
    return cnt
        
        
    

input = sys.stdin.readline

n,m = map(int,input().strip().split())

road = []
for _ in range(n):
    road.append(list(input().strip()))

for i in range(n):
    for j in range(m):
        if road[i][j] == 'I':
            road[i][j] = 'X'
            start = [i,j]
            break
            
answer = bfs(road,start,n,m)
if answer == 0:
    answer = 'TT'
print(answer)


