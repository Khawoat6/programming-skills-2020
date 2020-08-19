def Cola(n):
    s = n
    while (n>=3):
        c = n % 3
        n = n / 3
        s += n
        n += c
    if((n+1)%3 == 0):
        s += 1
    print(int(s))

n = int(input())
Cola(n)
