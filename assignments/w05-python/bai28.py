a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
op = input("Nhập phép toán (+, -, *, /): ")
if op == "+":
  res = a + b
elif op == "-":
  res = a - b
elif op == "*":
  res = a * b
elif op == "/":
  res = a / b if b != 0 else "Lỗi chia 0"
else:
  res = "Phép toán không hợp lệ"
print(f"Kết quả: {a} {op} {b} = {res}")