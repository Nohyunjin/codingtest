# 4

n, k = map(int, input().split())
a = list(map(int, input().split()))

res = set()

for i in range(n):
    for j in range(i+1, n):
        for h in range(j+1, n):
            res.add(a[i]+a[j]+a[h])

res = list(res)
res.sort(reverse=True)
print(res[k-1])