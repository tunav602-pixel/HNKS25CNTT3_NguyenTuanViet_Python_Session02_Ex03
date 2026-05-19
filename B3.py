# ==============================================================================
# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP (HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN NHẬP VIỆN)
# ==============================================================================

# ------------------------------------------------------------------------------
# A. PHÂN TÍCH INPUT / OUTPUT (Xác định rõ dữ liệu đầu vào và định dạng đầu ra)
# ------------------------------------------------------------------------------
# 1. DỮ LIỆU ĐẦU VÀO (INPUT):
#    - Tên bệnh nhân (name_patient): 
#      + Kiểu dữ liệu: Chuỗi ký tự (str).
#      + Điều kiện ràng buộc: Không được phép rỗng hoặc chỉ chứa khoảng trắng ("").
#    - Tuổi bệnh nhân (age_patient): 
#      + Kiểu dữ liệu: Số nguyên (int).
#      + Điều kiện ràng buộc: Phải nằm trong phạm vi sinh học hợp lý (0 <= tuổi <= 150).
#
# 2. ĐỊNH DẠNG ĐẦU RA (OUTPUT):
#    - Thông báo điều hướng (messenger): 
#      + Kiểu dữ liệu: Chuỗi ký tự (str).
#      + Định dạng hiển thị: Gồm tiền tố phân loại [ƯU TIÊN / KHÁM THƯỜNG], 
#        đối tượng cụ thể và chỉ dẫn phòng khám tương ứng.

# ------------------------------------------------------------------------------
# B. ĐỀ XUẤT GIẢI PHÁP (Kiểm tra lỗi và Phân luồng)
# ------------------------------------------------------------------------------
# Hệ thống được thiết kế theo mô hình 2 tầng kiểm duyệt để đảm bảo an toàn dữ liệu:
#
# TẦNG 1: KIỂM TRA LỖI DỮ LIỆU (Exception Handling & Validation)
#   - Sử dụng khối `try - except ValueError` để bắt lỗi khi ép kiểu dữ liệu từ chuỗi 
#     sang số nguyên (đối với biến age_patient).
#   - Sử dụng cấu trúc điều kiện độc lập `if` kết hợp phương thức `.strip()` để 
#     phát hiện và chặn trường hợp bỏ trống tên hoặc cố tình nhập khoảng trắng.
#   - Sử dụng toán tử logic `or` (`age_patient < 0 or age_patient > 150`) để gom 
#     2 vùng dữ liệu bất hợp lý của tuổi vào một nhánh xử lý duy nhất.
#   - Sử dụng `sys.exit()` để lập tức ngắt chương trình nếu phát hiện lỗi đầu vào.
#
# TẦNG 2: PHÂN LUỒNG NGHIỆP VỤ (Business Logic Triage)
#   - Sau khi dữ liệu đã "sạch", sử dụng cấu trúc điều kiện rẽ nhánh tuần tự 
#     `if - elif - else` để phân loại mức độ ưu tiên theo lứa tuổi:
#     + Nhánh 1 (`if age_patient >= 80`): Ưu tiên cho người cao tuổi.
#     + Nhánh 2 (`elif age_patient < 6`): Ưu tiên cho bệnh nhi.
#     + Nhánh 3 (`else`): Tất cả các độ tuổi còn lại (từ 6 đến 79) thuộc diện khám thường.

# ------------------------------------------------------------------------------
# C. THIẾT KẾ THUẬT TOÁN (Mô tả luồng chương trình bằng Pseudocode)
# ------------------------------------------------------------------------------
# BẮT ĐẦU CHƯƠNG TRÌNH
#
#   [BƯỚC 1: KIỂM TRA LỖI]
#   THỬ THỰC HIỆN:
#       Nhập name_patient
#       NẾU name_patient sau khi loại bỏ khoảng trắng là rỗng:
#           In thông báo: "Họ và tên không được để trống!"
#           Dừng chương trình.
#       Nhập age_patient và ép sang kiểu số nguyên
#       NẾU age_patient < 0 HOẶC age_patient > 150:
#           In thông báo: "Tuổi nằm ngoài phạm vi con người (0-150)!"
#           Dừng chương trình.
#   NẾU XẢY RA LỖI ĐỊNH DẠNG (ValueError):
#       In thông báo: "LỖI: Tên hoặc Tuổi không hợp lệ"
#       Dừng chương trình.
#
#   [BƯỚC 2: PHÂN LUỒNG NGHIỆP VỤ]
#   NẾU age_patient >= 80 THÌ:
#       messenger = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn..."
#   NẾU KHÔNG, NẾU age_patient < 6 THÌ:
#       messenger = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
#   NẾU KHÔNG (Tất cả trường hợp còn lại) THÌ:
#       messenger = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự..."
#
#   [BƯỚC 3: IN PHIẾU / HIỂN THỊ]
#   In giá trị của biến messenger ra màn hình.
#
# KẾT THÚC CHƯƠNG TRÌNH
# ==============================================================================

import sys


try:
    messenger = 0
    name_patient = input("Nhập tên bệnh nhân: ")

    if name_patient.strip() == "":
        print("Họ và tên không được để trống! Vui lòng nhập tên")
        sys.exit()
    age_patient = int(input("Nhập tuổi của bệnh nhân: "))

    if age_patient < 0 or age_patient > 150:
        print("Tuổi nằm ngoài phạm vi con người (0-150)!")
        sys.exit()

except ValueError:
    print("LỖI: Tên or Tuổi không hợp lệ ")
    sys.exit()

if age_patient >= 80:
    messenger = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
elif age_patient < 6:
    messenger = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
else:
    messenger = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print(messenger)
