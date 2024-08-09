def lozi(n):
    andazeh = 2 * n + 1
    for i in range(andazeh):
        if i <= n :
            fasele = n - i
            stars = 2 * i + 1
        else:
            fasele = i - n 
            stars = 2 * (andazeh - i - 1) + 1
        
        print(" " * fasele + "*" * stars)
    

n = int(input())

if n > 0:
    lozi(n)
