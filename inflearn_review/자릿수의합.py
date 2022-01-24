n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    res = 0
    while x > 0:
        res += x % 10
        x = x // 10
    return res

res = 0
max_num = 0

for i in a :
    son = digit_sum(i)
    if son > max_num:
        son = max_num
        res = i
print(res)