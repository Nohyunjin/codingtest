n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

tmp = n_list + m_list
res = sorted(tmp)

for x in res:
    print(x, end=' ')
