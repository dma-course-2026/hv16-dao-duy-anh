n = int(input("Nhập năm N: "))
nhuan = (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0)
print(f"Số ngày của năm {n} là {366 if nhuan else 365}")