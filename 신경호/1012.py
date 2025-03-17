'''
    bfs를 이용하여 풀이
'''
import sys
from collections import deque

input = sys.stdin.readline

def bfs(lt,m,n,i,j,answer):
    if lt[i][j] == 0:
        return answer
    else:
        q = deque()
        q.append([i,j])
        while q:
            tem = q.popleft()
            x,y = tem[0],tem[1]
            lt[x][y] = 0
            if y+1 < m and lt[x][y+1] ==1 :
                q.append([x,y+1])
                lt[x][y+1] = 0
            if  y-1>=0 and lt[x][y-1] == 1:
                q.append([x,y-1])
                lt[x][y-1] = 0
            if x-1 >= 0 and lt[x-1][y] == 1:
                q.append([x-1,y])
                lt[x-1][y] = 0
            if x+1 < n and lt[x+1][y] == 1:
                q.append([x+1,y])
                lt[x+1][y] = 0
        return answer+1
                

t = int(input().strip())
for _ in range(t):
    m,n,k = map(int,input().strip().split())
    answer = 0
    lt = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().strip().split())
        lt[y][x] = 1
    for i in range(n):
        for j in range(m):
            answer = bfs(lt,m,n,i,j,answer)
    print(answer)