def tinh_tong(n):
    if n == 1:
        return 1
    else:
        return n + tinh_tong(n-1)

# Nhập giá trị n từ người dùng
n = int(input("Nhập các số nguyên dương n = "))
# Gọi hàm tinh_tong để tính tổng
tong = tinh_tong(n)
# In kết quả
print("Tổng các số nguyên dương từ 1 đến", n, "là:", tong)
