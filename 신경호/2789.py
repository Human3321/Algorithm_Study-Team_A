#입력 단어에 검열 단어가 존재하는지 확인 후 삭제
#입력 단어를 확인하여 filler에 존재하면 건너뛰는 방식 사용

import sys

input = sys.stdin.readline

income = input()
filler = ['C','A','M','B','R','I','D','G','E']
answer = ''
for c in income:
    if c not in filler:
        answer += c
print(answer)