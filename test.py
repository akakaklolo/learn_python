def doi_tien(n, menh_gia):
    so_to_tien = [0,0,0, 0, 0, 0]
    for i in range(len(menh_gia)):
        so_to_tien[i] = n // menh_gia[i]
        n %= menh_gia[i]
    return so_to_tien


menh_gia = [500000,200000,100000, 50000, 20000, 10000]
n = int(input("nhập số tiền cần rút vào :"))
so_to_tien = doi_tien(n, menh_gia)
print(" cách mệnh giá của tiền cần rút là :")
for i in range(len(so_to_tien)):
    print(so_to_tien[i], "tờ", menh_gia[i], "đồng")
#cái này test thôi nha mấy cha