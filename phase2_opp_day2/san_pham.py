class SanPham:
    def __init__(self, ma_sp, ten_sp, gia_ban, so_luong):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.gia_ban = gia_ban
        self.so_luong = so_luong
        #class định nghĩa (định dạng đối tượng)
    
    def tinh_tong_gia_tri(self):
        return self.gia_ban * self.so_luong
        #phương thức tính tổng giá trị của đối tượng
    
    def hien_thi_thong_tin(self):
        print(f"[{self.ma_sp}] - {self.ten_sp} | Giá : {self.gia_ban:,}VND | Tồn {self.so_luong} | Tổng : {self.tinh_tong_gia_tri():,}VND")

        