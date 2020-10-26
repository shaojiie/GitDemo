from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
# driver = webdriver.Chrome()
# driver = webdriver.IEDriver();
driver = webdriver.Ie(executable_path="IEDriverServer.exe");
sql = "aa"
error_sql = "CREATE TABLE django_admin_log (id serial NOT NULL PRIMARY KEY, action_time datetime year to fraction(5) NOT NULL, object_id lvarchar(None) NULL, object_repr lvarchar(200) NOT NULL, action_flag smallint NOT NULL CHECK (action_flag >= 0), change_message lvarchar(None) NOT NULL, content_type_id integer NULL, user_id integer NOT NULL)"
replace_sql = "CREATE TABLE django_admin_log (id serial NOT NULL PRIMARY KEY, action_time datetime year to fraction(5) NOT NULL, object_id lvarchar(None) , object_repr lvarchar(200) NOT NULL, action_flag smallint NOT NULL CHECK (action_flag >= 0), change_message lvarchar(None) NOT NULL, content_type_id integer , user_id integer NOT NULL)"
if sql == error_sql:
	ql = replace_sql
print(sql)

#driver.maximize_window()
driver.implicitly_wait("1")
# url="https://email.picc.com.cn/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2femail.picc.com.cn%2fowa%2f"
# url="https://email.picc.com.cn/owa"
url="http://70.1.42.188/lpzb/"

driver.get(url)
# time.sleep(2)

driver.find_element_by_id('edtUserName').send_keys("5301000000")
driver.find_element_by_id('edtPassWord').send_keys("1111")

print(driver.find_element_by_id('edtPassWord'))
driver.find_element_by_id("btnLogin").click()

time.sleep(2)
driver.switch_to.frame("NaviFrame")

print("______dddddd________")
driver.find_elements_by_tag_name("a")[1].click()

driver.switch_to.parent_frame()
driver.switch_to.frame("MenuFrame")

print("______eeeeeee________")
print(driver.page_source)
# driver.find_element_by_link_text("未决案件清单").click()
print( driver.find_elements_by_id("TreeView_y2020lpjkt48"))
print( driver.find_elements_by_id("TreeView_y2020lpjkn47"))
driver.find_elements_by_id("TreeView_y2020lpjkn47")[0].click()
driver.find_elements_by_id("TreeView_y2020lpjkt48")[0].click()

# driver.find_element(By.linkText("未决发展监控（地市）")).click()
driver.switch_to.parent_frame()
driver.switch_to.frame("MainFrame")

# print(driver.page_source)
# driver.find_elements_by_id("MyGridView_ctl03_lbltjdate")[0].get_attribute()
atrbute = driver.find_elements_by_id("MyGridView_ctl04_lbltjdate")

print(atrbute[0].text )
print(driver.find_elements_by_id("MyGridView_ctl03_lblcomname")[0].text )

print(atrbute[0].get_attribute("id"))
# driver.find_elements_by_id("MyGridView_ctl04_lbltjdate")[0].linkText
