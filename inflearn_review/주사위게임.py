# def prize(a, b, c):
#     if (a == b) & (a == c):
#         return 10000 + 1000 * a
#     elif (a == b) | (b == c):
#         return 1000 + 1000 * b
#     else :
#         return c * 100
    
n = int(input())

res = 0
tmp = 0

for i in range(n) :
    g = list(map(int, input().split()))
    g.sort()
    if (g[0] == g[1]) & (g[1] == g[2]):
        tmp = 10000 + 1000 * g[0]
    elif (g[0] == g[1]) | (g[1] == g[2]):
        tmp = 1000 + 100 * g[1]
    elif (g[0] != g[1]) & (g[1] != g[2]):
        tmp = g[2] * 100
    if tmp > res:
        res = tmp

print(res)

# import sys
# sys.stdin=open("섹션 2/9. 주사위 게임/in1.txt", "r")
# n = int(input())

# max=0
# for i in range(n):
#     money = 0
    
#     dice = list(map(int, input().split()))
#     dice.sort()
#     a, b, c = 0, 1, 2
    
#     if (dice[a] == dice[b]) & (dice[b] == dice[c]):
#         money = 10000 + dice[a]*1000
#     elif (dice[a] == dice[b]) | (dice[b] == dice[c]):
#         money = 1000 + dice[b]*100
#     elif (dice[a] != dice[b]) & (dice[b] != dice[c]):
#         money = dice[c]*100

#     if money > max:
#         max = money
        
# print(max)