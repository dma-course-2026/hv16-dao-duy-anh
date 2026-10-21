a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
res = []
if a != 0 and b % a == 0:
  res.append(f"{a} là ước của {b}")
if b != 0 and a % b == 0:
  res.append(f"{b} là ước của {a}")
print(", ".join(res) if res else "Không là ước của nhau.")