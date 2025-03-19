'''
    그래프 탐색
    dic을 이용해서 그래프 작성
    
'''

import sys
from collections import deque
input = sys.stdin.readline

v = int(input().strip())
e = int(input().strip())
dic = {k:[] for k in range(1,v+1)}
for _ in range(e):
    start,end = map(int,input().strip().split())
    dic[start].append(end)
    dic[end].append(start)

q = deque()
lt = [0 for _ in range(v+1)]
q.append(1)
lt[1] = 1
cnt = 0


while q:
    now = q.popleft()
    for d in dic[now]:
        if lt[d] == 0:
            lt[d] = 1
            q.append(d)
            cnt +=1
print(cnt)
            


