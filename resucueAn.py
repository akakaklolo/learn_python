def rescue_an(k, m):
    dp = [0] * (m + 1)
    for i in range(1, m + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            dp[i] = min(dp[i], max(dp[j - 1], dp[i - j]) + 1)
        dp[i] = min(dp[i], i * (i + 1) // 2)
    return dp[m]

n = int(input())
for _ in range(n):
    k, m = map(int, input().split())
    print(rescue_an(k, m))
