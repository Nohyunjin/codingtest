def prize(a, b, c):
    if a == b & a == c:
        return 10000 + 1000 * a
    elif a == b | b == c:
        return 1000 + 1000 * a
    elif b == c:
        return 1000 + 1000 * c
    else :
        return max(a, b, c)* 100
    
n = int(input())

res = []

for i in range(n) :
    a = list(map(int, input().split()))
    tmp = prize(a[0], a[1], a[2])
    res.append(tmp)

print(max(res))