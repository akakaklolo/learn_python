t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    while n > 1:
        if n % 6 == 0:
            n //= 6
            count += 1
        elif n % 3 == 0:
            n //= 3
            count += 2
        else:
            break
    if n == 1:
        print(count)
    else:
        print(-1)
