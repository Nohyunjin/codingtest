# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고
# 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 작성해서 프로그래밍 하세요.

def digit_sum(x):
    res = 0
    while x > 0 :
        if x % 10 > 0:
            res += x % 10
            x = x // 10
        elif x % 10 == 0 :
            break
    return res

n = int(input())
a = list(map(int, input().split()))

res = 0
max_ = -1

for i in a:
    son = digit_sum(i)
    if son > max_:
        max_ = son
        res = i
print(res)