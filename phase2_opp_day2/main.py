import csv
from san_pham import SanPham


def luu_csv(danh_sach_sp):
    with open("san_pham.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ma_sp", "ten_sp", "gia_ban", "so_luong"])
        for sp in danh_sach_sp:
            writer.writerow([sp.ma_sp, sp.ten_sp, sp.gia_ban, sp.so_luong])
    print(">> Đã lưu dữ liệu vào san_pham.csv thành công!")


def doc_csv():
    ds = []
    try:
        with open("san_pham.csv", mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sp = SanPham(
                    row["ma_sp"],
                    row["ten_sp"],
                    int(row["gia_ban"]),
                    int(row["so_luong"]),
                )
                ds.append(sp)
    except FileNotFoundError:
        pass

    return ds


# 1. ĐỌC DỮ LIỆU CŨ TỪ FILE KHI MỞ APP
danh_sach_sp = doc_csv()

while True:
    print("\n--- QUẢN LÝ KHO HÀNG ---")
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Thoát")

    chon = input("Nhập lựa chọn (1-3): ")

    if chon == "1":
        if not danh_sach_sp:
            print(">> Kho hàng đang trống!")
        else:
            print("\n=== DANH SÁCH SẢN PHẨM IN KHO ===")
            tong_toan_kho = 0
            for sp in danh_sach_sp:
                sp.hien_thi_thong_tin()
                tong_toan_kho += sp.tinh_tong_gia_tri()
            print(f"===> TỔNG GIÁ TRỊ TOÀN KHO: {tong_toan_kho:,} VNĐ")

    elif chon == "2":
        print("\n=== NHẬP SẢN PHẨM MỚI ===")
        ma = input("Nhập mã SP: ")
        ten = input("Nhập tên SP: ")
        gia = int(input("Nhập giá bán: "))
        so_luong = int(input("Nhập số lượng: "))

        sp_moi = SanPham(ma, ten, gia, so_luong)
        danh_sach_sp.append(sp_moi)

        # 2. TỰ ĐỘNG LƯU RA FILE CSV NGAY KHI THÊM MỚI
        luu_csv(danh_sach_sp)

    elif chon == "3":
        print("Cảm ơn sếp đã sử dụng chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")