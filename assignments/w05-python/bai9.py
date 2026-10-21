ho_ten = input("Nhập họ tên chủ hộ: ")
cu, moi = map(int, input("Nhập chỉ số cũ và mới: ").split())
tieu_thu = moi - cu
if tieu_thu <= 60:
  tien = tieu_thu * 5
elif tieu_thu <= 160:
  tien = 60 * 5 + (tieu_thu - 60) * 8
else:
  tien = 60 * 5 + 100 * 8 + (tieu_thu - 160) * 10
print(f"Chủ hộ {ho_ten} tiêu thụ {tieu_thu} kW -> Số tiền: {tien:.2f}")