# import sys
# sys.stdin = open("inflearn_review/input.txt", 'r')

def reverse(x) :
    a = 0
    while x > 0:
        t=x%10
        a=a*10+t
        x //= 10
    return(a)

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

res = []

for i in range(n):
    if is_prime(reverse(a[i])) == True:
        res.append(reverse(a[i]))
print(res, end=" ")