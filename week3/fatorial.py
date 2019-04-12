def fatorial(n):
    if n < 0:
        return 0
    fat = 1
    while(n > 1):
        fat = fat * n
        n = n - 1 
    return fat