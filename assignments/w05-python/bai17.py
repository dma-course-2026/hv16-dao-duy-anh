a = float(input("Nhập cạnh 1: "))
b = float(input("Nhập cạnh 2: "))
c = float(input("Nhập cạnh 3: "))
canh = sorted([a, b, c])
if (
    canh[0] + canh[1] > canh[2]
    and abs(canh[0] ** 2 + canh[1] ** 2 - canh[2] ** 2) < 1e-9
):
  print("Là tam giác vuông.")
else:
  print("Không phải tam giác vuông.")