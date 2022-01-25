import sys
sys.stdin=open("inflearn\input.txt", "r")

n = int(input())
gam = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    gam.append(gam[trunc(n%i)])