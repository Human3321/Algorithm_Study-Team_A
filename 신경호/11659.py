#메모리제이션 사용
#리스트를 사용하여 이전까지의 합에 대한 값 사용
#idx를 통해 값을 불러서 뺄샘

import sys

input = sys.stdin.readline

n,m = map(int,input().strip().split())

lt = list(map(int,input().strip().split()))

sum_lt = [0 for _ in range(n+1)]
for i in range(1,n+1):
    sum_lt[i] += sum_lt[i-1] + lt[i-1]
        
for _ in range(m):
    start,end = map(int,input().strip().split())
    answer = sum_lt[end] - sum_lt[start-1]
    print(answer)