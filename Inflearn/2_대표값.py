k = int(input())
a = list(map(int, input().split()))
ave = int(sum(a)/len(a) + 0.5)
print(ave)
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if 