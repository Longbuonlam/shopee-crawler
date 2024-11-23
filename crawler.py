from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
# Đường dẫn tới ChromeDriver
chrome_driver_path = '/Users/mac/Downloads/chromedriver-mac-arm64/chromedriver'
 
# Khởi tạo Service cho ChromeDriver
service = Service(executable_path=chrome_driver_path)
 
# Khởi tạo trình duyệt với Service
driver = webdriver.Chrome(service=service)
 
# Truy cập vào trang web
url = 'https://shopee.vn/daily_discover?pageNumber=2&is_from_login=true'
driver.get(url)
 
# Chờ một thời gian ngắn để trang tải toàn bộ nội dung
time.sleep(2)

#Type email
email_field = driver.find_element(By.NAME, 'loginKey')
email_field.send_keys('your_email@example.com')

email_field.send_keys(Keys.TAB)
time.sleep(1) 

#Type password
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('your_password')
time.sleep(2)

# Click login button
login_button = driver.find_element(By.CSS_SELECTOR, 'button.b5aVaf.PVSuiZ.Gqupku.qz7ctP.qxS7lQ.Q4KP5g')
if login_button:
    print("Login button found")
    login_button.click()
else:
    print("Login button not found")

time.sleep(5)
 
#quit program
driver.quit()
 