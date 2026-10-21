h = int(input("Nhập giờ: "))
p = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
total = (h * 3600 + p * 60 + s + 1) % 86400
nh, rem = divmod(total, 3600)
np, ns = divmod(rem, 60)
print(f"{nh} {np} {ns}")