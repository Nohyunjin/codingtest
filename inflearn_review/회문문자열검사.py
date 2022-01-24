n = int(input())

for i in range(n):
    a = input()
    a = a.upper()
    if a == a[::-1]:
        print(f"#{i+1} YES")
    else :
        print(f"#{i+1} NO")
    