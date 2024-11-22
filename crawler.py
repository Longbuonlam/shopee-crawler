from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
 
# Đường dẫn tới ChromeDriver (bạn cần chỉnh đúng vị trí trên máy của bạn)
chrome_driver_path = '/Users/mac/Downloads/chromedriver-mac-arm64/chromedriver'
 
# Khởi tạo Service cho ChromeDriver
service = Service(executable_path=chrome_driver_path)
 
# Khởi tạo trình duyệt với Service
driver = webdriver.Chrome(service=service)
 
# Truy cập vào trang web
url = 'https://shopee.vn/daily_discover?pageNumber=2&is_from_login=true'
driver.get(url)
 
# Chờ một thời gian ngắn để trang tải toàn bộ nội dung
time.sleep(5)
 
# Lấy mã nguồn HTML của trang sau khi đã tải JavaScript
html_content = driver.page_source
 
# Đóng trình duyệt sau khi lấy được mã nguồn
driver.quit()
 
# Nếu muốn lưu vào file HTML
with open('2shopee_page_source.html', 'w', encoding='utf-8') as file:
    file.write(html_content)