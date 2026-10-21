import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
  cv = a + b + c
  p = cv / 2
  s = math.sqrt(p * (p - a) * (p - b) * (p - c))
  print(f"Chu vi {cv:.2f}, Diện tích {s:.2f}")
else:
  print("Không tạo thành tam giác.")