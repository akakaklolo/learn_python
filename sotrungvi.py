def median_of_three(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

def nhap_ba_so():
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    c = int(input("Nhập số thứ ba: "))
    return (a, b, c)

my_tuple = nhap_ba_so()
result = median_of_three(*my_tuple)
print(f"Số trung vị của {my_tuple} là {result}")
