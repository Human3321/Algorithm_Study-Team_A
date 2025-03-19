'''
    heapq 라이브러리를 이용
    튜플 형식으로 (abs(i),i)로 힙을 구성하자
'''

import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

heap = []
for _ in range(n):
    tem = int(input().strip())
    if tem == 0:
        if heap:
            p = heapq.heappop(heap)
            print(p[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(tem),tem))