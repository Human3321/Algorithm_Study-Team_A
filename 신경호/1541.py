'''
    1.-로 split
    2.나누어진 리스트를 sum
    3.첫번째 리스트에서 나머지 리스트를 뺀다
'''

import sys

input = sys.stdin.readline

lt = input().strip().split('-')
answer = []
for t in lt:
    tem = list(map(int,t.split('+')))
    tem = sum(tem)
    answer.append(tem)
frist = answer[0]
for value in range(1,len(answer)):
    frist = frist - answer[value]
print(frist)
    