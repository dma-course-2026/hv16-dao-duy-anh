a, b, c = map(float, input("Nhập 3 điểm: ").split())
dtb = (a + b + c) / 3
trang_thai = "Đậu" if dtb >= 5.0 else "Rớt"
print(f"Điểm trung bình là: {dtb:.2f}, {trang_thai}")