# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를
# 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

# import sys
# sys.stdin=open("input.txt", "r")

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

tmp = n_list + m_list
res = sorted(tmp)

for x in res:
    print(x, end=' ')

