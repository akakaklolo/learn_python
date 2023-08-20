# Ví dụ:


def count_consecutive_sums(N):
    count = 0
    i = 1
    while i * (i + 1) // 2 <= N:
        if (N - i * (i + 1) // 2) % (i + 1) == 0:
            count += 1
        i += 1
    return count

# Test case với N = 10^16
N = int(input("nhập N"))
result = count_consecutive_sums(N)
print("Số cách chia số", N, "thành tổng các số nguyên dương liên tiếp là:", result)
