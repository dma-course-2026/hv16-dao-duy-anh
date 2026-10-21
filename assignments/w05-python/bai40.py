m = int(input("Nhập M: "))
n = int(input("Nhập N: "))
tong = sum(i for i in range(m, n + 1) if i % 3 == 0 or i % 5 == 0)
print(f"Kết quả: {tong}")