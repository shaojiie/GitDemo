from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
driver = webdriver.Chrome()
#driver.maximize_window()
#driver.implicitly_wait("1")
# url="https://email.picc.com.cn/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2femail.picc.com.cn%2fowa%2f"
# url="https://email.picc.com.cn/owa"
url="https://email.picc.com.cn/owa/"

driver.get(url)
# time.sleep(2)

driver.find_element_by_id('username').send_keys("shaojie03")
driver.find_element_by_id('password').send_keys("pass@word7")

driver.find_element_by_class_name("btn").click()
