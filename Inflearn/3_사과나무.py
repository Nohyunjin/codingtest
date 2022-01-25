import sys
sys.stdin=open("inflearn\input.txt", "r")

n = int(input())
a_tree = [list(map(int, input().split())) for _ in range(n)]

sum_ = 0
lt = n//2
rt = n//2

for i in range(n):
    for j in range(lt, rt + 1):
        sum_ += a_tree[i][j]
    if i < n//2:
        lt -= 1
        rt += 1
    else :
        lt += 1
        rt -= 1
print(sum_)