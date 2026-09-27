#1. Bản thiết kế khách hàng 
class KhachHang:
    def __init__(self, ma_kh, ho_ten, so_dien_thoai, doanh_so):
        self.ma_kh = ma_kh
        self.ho_ten = ho_ten
        self.so_dien_thoai = so_dien_thoai
        self.doanh_so = doanh_so

    
    #phương thức phân loại
    def tinh_phan_loai(self):
        
     phan_loai = "VIP" if self.doanh_so >= 10000000 else "NORMAL"
     return phan_loai

    #phương thức (hàm{hành động}) hiển thị thông tin
    def hien_thi_thong_tin(self):
        print(f"[{self.ma_kh}] - {self.ho_ten} | sdt: {self.so_dien_thoai} | doanh số :{self.doanh_so} | phân loại : {self.tinh_phan_loai()}")


#2. tạo các đối tượng (object) thực tế
kh1 = KhachHang("KH01", "Nguyen Van A", "0987654321", 15000000)
kh2 = KhachHang("KH02", "Tran Thi B", "0123456789", 4500000)

#gọi tên hàm hthi
kh1.hien_thi_thong_tin()
kh2.hien_thi_thong_tin()