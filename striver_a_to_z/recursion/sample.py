

def recursive(n):
    print(n)
    if n == -10:
        return n
    return recursive(n-1)

recursive(10)