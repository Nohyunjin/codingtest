N = int(input())
num_list = list(map(int,(input().split())))
count = 0

for i in num_list :
    cnt = 0
    if i == 1:
        continue
    for k in range(2, i+1):
        if i % k == 0:
            cnt += 1
    if cnt == 1:
        count += 1
print(count)