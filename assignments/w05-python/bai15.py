a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a and a == b == c:
  print("Là tam giác đều.")
else:
  print("Không phải tam giác đều.")