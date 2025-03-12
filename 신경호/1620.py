#첫 줄은 포켓몬 n개와 맞춰야하는 m개의 질문
#딕셔너리로 포켓몬을 저장
#반대 경우의 dic을 생성

import sys

input = sys.stdin.readline

n,m = map(int,input().strip().split())

dic = {}
for i in range(1,n+1):
    dic[i] = input().strip()
dic_value = { v:k for k,v in dic.items()}

for _ in range(m):
    ch = input().strip()
    if ch.isdigit():
        print(dic.get(int(ch)))
    else:
        print(dic_value.get(ch))

