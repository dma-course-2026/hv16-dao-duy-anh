import math

x0 = float(input("Nhập x0: "))
y0 = float(input("Nhập y0: "))
r = float(input("Nhập R: "))
xa = float(input("Nhập xa: "))
ya = float(input("Nhập ya: "))
d = math.sqrt((xa - x0) ** 2 + (ya - y0) ** 2)
if abs(d - r) < 1e-9:
  print("Nằm trên đường tròn.")
elif d < r:
  print("Nằm trong đường tròn.")
else:
  print("Nằm ngoài đường tròn.")