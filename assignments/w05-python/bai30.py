s = int(input("Nhập số giây: "))
h, rem = divmod(s, 3600)
m, sec = divmod(rem, 60)
print(f"{h} giờ : {m} phút : {sec} giây")