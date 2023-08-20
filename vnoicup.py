
import math
n = int(input())
a =list(map(int, input().split()))
def so_mang_a(a,x):
    if len(a) < n :
        return False
for i in range (a):
    ucln = math.gcd(a[i], a[i+1])

