from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
driver = webdriver.Chrome()
#driver.maximize_window()
driver.implicitly_wait("3")
# url="https://email.picc.com.cn/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2femail.picc.com.cn%2fowa%2f"
# url="https://email.picc.com.cn/owa"
url="http://70.1.42.188/lpzb/"

driver.get(url)
time.sleep(2)

# e_mail
# driver.find_element_by_id('username').send_keys("shaojie03")
# print(driver.find_element_by_id('username'))
# driver.find_element_by_id('password').send_keys("pass@word6")
# driver.find_element_by_css_selector("[type=submit]").click()
# time.sleep(4)

driver.find_element_by_id('edtUserName').send_keys("5301000000")
driver.find_element_by_id('edtPassWord').send_keys("1111")
driver.find_element_by_id("btnLogin").click()



driver.find_element(By.XPATH("//img[@href='Menu.aspx?activeview=0']"));


# img[@href='http://www.baidu.com']

# <img src="images/menu0.gif" alt="" style="border-style:none;vertical-align:middle;">
# print(driver.find_elements_by_name("Menu1_1"))
# s20 = driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/a/img").click()
# driver.find_elements_by_class_name("Menu1_1").click()
# ref="Menu.aspx?activeview=0"
# driver.get(ref)



# <a class="Menu1_1" href="Menu.aspx?activeview=0" target="MenuFrame"><img src="images/menu0.gif" alt="" style="border-style:none;vertical-align:middle;"></a>
# /html/body/form/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/a/img
# <a class="Menu1_1" href="Menu.aspx?activeview=0" target="MenuFrame"><img src="images/menu0.gif" alt="" style="border-style:none;vertical-align:middle;"></a># //*[@id="Menu1n0"]/td/table/tbody/tr/td/a/img
# # //*[@id="Menu1n1"]/td/table/tbody/tr/td/a/img
# //*[@id="Menu1n1"]/td/table/tbody/tr/td/a/img
# <img src="images/menu0.gif" alt="" style="border-style:none;vertical-align:middle;">

# //*[@id="Menu1n0"]/td/table/tbody/tr/td/a/img
#driver.quit()
