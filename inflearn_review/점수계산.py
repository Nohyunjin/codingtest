n = int(input())
a = list(map(int, input().split()))

cnt = 0
sum_ = 0

for i in range(n):
    if a[i] == 1:
        cnt += 1
        sum_ += cnt
    else:
        cnt = 0
print(sum_)