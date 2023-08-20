n = int(input())
lst = list(map(int, input().split()))

def is_arithmetic_sequence(lst):
    if len(lst) < 2:
        return False
    diff = lst[1] - lst[0]
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != diff:
            return False
    return True

if is_arithmetic_sequence(lst):
    print("YES")
else:
    print("NO")
    