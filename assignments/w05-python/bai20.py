import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a == 0:
  if b == 0:
    print("Vô số nghiệm" if c == 0 else "Vô nghiệm")
  else:
    print(f"Phương trình bậc 1 có nghiệm: x = {-c/b}")
else:
  delta = b**2 - 4 * a * c
  if delta < 0:
    print("Phương trình vô nghiệm.")
  elif delta == 0:
    print(f"Nghiệm kép x = {-b/(2*a)}")
  else:
    print(
        f"x1 = {(-b + math.sqrt(delta))/(2*a)}, x2 ="
        f" {(-b - math.sqrt(delta))/(2*a)}"
    )