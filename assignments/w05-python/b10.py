n = int(input("Nhập số có 3 chữ số: "))
tram = n // 100
chuc = (n % 100) // 10
don_vi = n % 10
print(f"hàng trăm = {tram}, hàng chục = {chuc}, hàng đơn vị = {don_vi}")