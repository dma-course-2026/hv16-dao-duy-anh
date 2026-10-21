a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0:
  print("Đúng với mọi x" if b >= 0 else "Vô nghiệm")
elif a > 0:
  print(f"x >= {-b/a}")
else:
  print(f"x <= {-b/a}")