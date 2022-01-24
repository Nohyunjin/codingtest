# import sys
# sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())

res = []

try:
    for i in range(1, n + 1):
        if n % i == 0 :
            res.append(i)
    print(res[k-1])
    
except:
    print(-1)