n = int(input())

for i in range(n):
    a = input()
    a = a.upper()
    if a == a[::-1]:
        print(f"#")
    