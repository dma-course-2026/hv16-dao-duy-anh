a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
m = float(input("Nhập m: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
n = float(input("Nhập n: "))
D, Dx, Dy = a * d - b * c, m * d - b * n, a * n - m * c
if D != 0:
  print(f"x ≈ {Dx/D:.3f}, y ≈ {Dy/D:.3f}")
elif Dx == 0 and Dy == 0:
  print("Vô số nghiệm.")
else:
  print("Vô nghiệm.")