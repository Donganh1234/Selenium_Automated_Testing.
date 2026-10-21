# Selenium_Automated_Testing.
1. Giới thiệu

1.1. Mục tiêu

Bài thực hành nhằm tìm hiểu và ứng dụng Selenium WebDriver để xây dựng chương trình kiểm thử tự động cho website. Thông qua bài tập, sinh viên làm quen với việc điều khiển trình duyệt bằng Python, thực hiện các thao tác trên giao diện web và sử dụng pytest để kiểm tra kết quả thực tế so với kết quả mong đợi.

1.2. Website kiểm thử

Tên website: SauceDemo

Địa chỉ: https://www.saucedemo.com/

Loại website: Website mô phỏng bán hàng trực tuyến.

Phạm vi kiểm thử: Đăng nhập, xử lý đăng nhập sai, sắp xếp sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất.

2. Công cụ và môi trường thực hiện

Thành phần

Công cụ / Phiên bản

Hệ điều hành

Windows

Ngôn ngữ lập trình

Python 3.14.4

Công cụ tự động hóa

Selenium WebDriver 4.51.0

Framework kiểm thử

pytest 9.1.1

Trình duyệt

Google Chrome

Trình soạn thảo

Visual Studio Code

2.1. Các thư viện sử dụng

selenium: Điều khiển trình duyệt và tương tác với các phần tử trên website.

pytest: Tổ chức, thực thi và báo cáo kết quả các test case.

3. Danh sách test case

Bài thực hành xây dựng 05 test case kiểm thử tự động như sau:

Mã test case

Chức năng

Dữ liệu kiểm thử

Kết quả mong đợi

TC01

Đăng nhập thành công

Username: standard_user; Password: secret_sauce

Đăng nhập thành công và hiển thị trang Products

TC02

Đăng nhập thất bại

Username: standard_user; Password: wrong_password

Hiển thị thông báo lỗi đăng nhập

TC03

Sắp xếp sản phẩm

Chọn sắp xếp theo giá tăng dần

Giá các sản phẩm được sắp xếp theo thứ tự tăng dần

TC04

Thêm sản phẩm vào giỏ hàng

Sauce Labs Backpack

Sản phẩm được thêm vào giỏ hàng và số lượng hiển thị là 1

TC05

Đăng xuất

Tài khoản đã đăng nhập thành công

Đăng xuất và quay lại trang đăng nhập

4. Cài đặt và thực thi

4.1. Cài đặt môi trường

Cài đặt Python và Google Chrome, sau đó tạo môi trường ảo:

python -m venv venv

Kích hoạt môi trường ảo trên Windows PowerShell:

.\venv\Scripts\Activate.ps1

Cài đặt các thư viện cần thiết:

pip install selenium pytest

4.2. Thực thi chương trình

Đặt terminal tại thư mục chứa file test_saucedemo.py, sau đó chạy lệnh:

python -m pytest -v

Selenium WebDriver tự động mở trình duyệt Chrome để thực hiện các thao tác kiểm thử. Pytest ghi nhận trạng thái của từng test case dựa trên các điều kiện kiểm tra được định nghĩa trong chương trình.

5. Kết quả kiểm thử

Chương trình đã được thực thi trên môi trường Windows bằng Python, Selenium WebDriver và pytest.

Kết quả ghi nhận từ lần chạy thực tế:

Mã test case

Nội dung kiểm thử

Kết quả

TC01

Đăng nhập thành công

PASSED

TC02

Đăng nhập với mật khẩu sai

PASSED

TC03

Sắp xếp sản phẩm theo giá tăng dần

PASSED

TC04

Thêm sản phẩm vào giỏ hàng

PASSED

TC05

Đăng xuất khỏi hệ thống

PASSED

Tổng kết kết quả:

Tổng số test case: 5

Số test case thành công: 5

Số test case thất bại: 0

Thời gian thực thi: 18,10 giây

5.1. Hình ảnh minh chứng

Ảnh chụp màn hình dưới đây minh họa kết quả thực thi tự động của 05 test case bằng pytest.



6. Cấu trúc dự án

Selenium_Testing/
├── test_saucedemo.py
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
    └── selenium_test_results.png

Trong đó:

test_saucedemo.py: Chứa mã nguồn của 05 test case.

README.md: Tài liệu báo cáo và hướng dẫn thực hiện.

requirements.txt: Danh sách thư viện cần cài đặt.

.gitignore: Quy định các file và thư mục không đưa lên GitHub.

screenshots/: Lưu ảnh minh chứng kết quả kiểm thử.

7. Kết luận

Thông qua bài thực hành, sinh viên đã tìm hiểu và áp dụng Selenium WebDriver kết hợp với Python và pytest để kiểm thử tự động các chức năng cơ bản của một website thương mại điện tử.

Chương trình thực hiện thành công 05 test case, bao gồm đăng nhập hợp lệ, đăng nhập không hợp lệ, sắp xếp sản phẩm, thêm sản phẩm vào giỏ hàng và đăng xuất. Kết quả thực nghiệm cho thấy các điều kiện kiểm thử được xác định đều thỏa mãn trong lần chạy đã ghi nhận.

Bài thực hành giúp củng cố kiến thức về kiểm thử phần mềm, cách xây dựng test case tự động và cách sử dụng công cụ để kiểm tra chức năng của website.
