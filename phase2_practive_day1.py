class SanPham:
    def __init__(self, ma_sp, ten_sp, gia_ban, so_luong):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.gia_ban = gia_ban
        self.so_luong = so_luong

    def tinh_tong_gia_tri(self):
        return self.gia_ban * self.so_luong

    def hien_thi_thong_tin(self):
        print(f"{self.ma_sp} - {self.ten_sp} | Giá {self.gia_ban} | Tồn kho: {self.so_luong} | Tổng Giá trị kho {self.tinh_tong_gia_tri()}")

sp1 = SanPham("SP01", "Laptop Dell", 15000000, 5)
sp2 = SanPham("SP02", "Chuot Logitech", 30000, 20)
danh_sach_sp = [sp1, sp2]

for sp in danh_sach_sp: 
    sp.hien_thi_thong_tin()

tong_kho = 0
for sp in danh_sach_sp:
    tong_kho += sp.tinh_tong_gia_tri()
print(f"===> Tổng giá trị toàn bộ kho hàng là : {tong_kho} VND")

