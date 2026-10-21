a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
thuong = a / b if b != 0 else "Không chia được"
print(f"Tổng {a + b}, Hiệu {a - b}, Tích {a * b}, Thương {thuong}.")