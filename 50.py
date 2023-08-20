def tinh_diem(n):
    diem = 0
    phat_trung = 0
    phat_bo_loi = 14

    for i in range(1, n + 1):
        if i == phat_bo_loi:
            phat_trung =0
        
            phat_bo_loi =+15

        if phat_trung > 9 :
            diem += 1
        else:
            diem += 2

        phat_trung += 1

    return diem

n = int(input("Nhập số phát bắn đầu tiên: "))
diem = tinh_diem(n)
print(f"Điểm đạt được từ {n} phát bắn đầu tiên: {diem}")
