a = input()

tmp = []

for i in range(len(a)):
    if a[i].isdigit() == True:
        tmp.append(a[i])
    else:
        pass
res = ''.join(tmp)
res = int(res)
print(res)

tmp2 = []

for i in range(1,res+1):
    if res % i == 0:
        tmp2.append(i)
print(len(tmp2))