a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0:
  print("Vô số nghiệm" if b == 0 else "Vô nghiệm")
else:
  print(f"Phương trình có một nghiệm: x = {-b/a}")