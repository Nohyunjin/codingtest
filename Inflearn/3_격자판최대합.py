# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.


# import sys
# sys.stdin=open("inflearn\input.txt", "r")

n = int(input())
a = []

for i in range(n):
    m = list(map(int, input().split()))
    a.append(m)

sum_list = []

for i in range(n):
    sum_tmp = 0
    sum_tmp1 = 0
    for j in range(n):
        sum_tmp += a[i][j]
        sum_tmp1 += a[j][i]
    sum_list.append(sum_tmp)
    sum_list.append(sum_tmp1)

if n%2 == 1: 
    sum_tmp2 = 0
    for i in range(n):
        sum_tmp2 += a[i][i]
    sum_list.append(sum_tmp2)

    sum_tmp3 = 0
    for i in range(n):
        sum_tmp3 += a[n-i-1][i]
    sum_list.append(sum_tmp3)

else :
    pass

print(max(sum_list))