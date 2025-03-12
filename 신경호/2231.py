# 1에서 부터 n까지 올라가면서 정답 서치
# n은 최대 1,000,000
import sys

input = sys.stdin.readline

value = int(input())
answer = 0
for i in range(1,value):
    if i + sum(map(int,str(i))) == value: #i를 문자열로 변환한 다음 map을 이용하여 각 자릿수를 int로 변환하여 sum
        answer = i
        break

print(answer)
        