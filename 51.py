
def sum_of_divisors(lst):
    divisors = [1]
    for i in range(2, int(lst**(0.5))+1):
        if lst % i == 0:
            divisors.extend([i, lst//i])
    return sum(set(divisors))

q = int(input())
levels = list(map(int, input().split()))

for level in levels:
    boss_strength = sum_of_divisors(level)
    print(boss_strength, end=' ')