n = int(input("Nhập số lượng phần tử của dãy: "))
count = 0
for i in range(10**n):
    a = [int(d) for d in str(i).zfill(n)]
    if min(a) == 0 and max(a) == 9:
        count += 1
print("Số dãy thỏa mãn điều kiện là:", count)
