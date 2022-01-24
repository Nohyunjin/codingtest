n = int(input())

def prime_list(n):
    ch = [True] * n
    m = int(n ** 0.5)
    
    for i in range(2, m + 1):
        if ch[i] == True:
            for ch[j] in range(2 * i, n, i):
                ch[j] = False
                
    return [i for i in range(2, n) if ch[i] == True]

len(prime_list(n))