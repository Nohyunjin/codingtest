# import sys
# sys.stdin=open("input.txt", "r")
# 1에서 20까지의 숫자를 리스트로 배치
a=list(range(21))
# for 문을 통해 총 10번의 조건을 돌림
for i in range(10):
    # 배열의 범위를 받는 input 값을 n과 m에 전달
    n, m=map(int, input().split())
    # 범위의 중위수만큼 for문을 돌려서 배치를 바꿔 주는 중첩 for문
    for j in range((m-n+1)//2):
        a[n+j], a[m-j] = a[m-j], a[n+j]
a.pop(0)
for x in a:
    print(x, end=' ')