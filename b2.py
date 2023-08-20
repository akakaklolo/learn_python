def count_consecutive_sums(N):
    count = 0
    for i in range(1, N):
        sum = 0
        for j in range(i, N):
            sum += j
            if sum == N:
                count += 1
                break
            elif sum > N:
                break
    return count
#
# Ví dụ:
N = 10**16
result = count_consecutive_sums(N)
print("Số cách chia số", N, "thành tổng các số nguyên dương liên tiếp là:", result)

