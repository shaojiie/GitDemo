#!/usr/bin/python
# -*-coding:utf-8-*-
import pypyodbc

#com = pypyodbc.connect(connectString) charset='utf8'
conn =pypyodbc.connect('DRIVER={IBM INFORMIX ODBC DRIVER};SERVER=yndbsvr3;DATABASE=yn5301;UID=query;PWD=query333'\
	,encoding='GBK')
	#,charset="utf8")

#conn = pypyodbc.connect('DSN=32_yn5301')#,unicode_results=False)
#conn.setencoding(encoding='GBK')
 
cr = conn.cursor()
#re = conn.cursor().execute('SELECT * FROM lpzx_yjqd').fetchone()[0].decode('UTF-8')
sql = "select first 2 * from lpzx_usercode "
#print(results[0])
#sql = "insert into lpzx_usercode values ('测试','组','11111111','咔咔咔','','DDD')"
# (groupname, usercode,username) VALUES (?, ?,?)"
#sql = "INSERT INTO lpzx_usercode (groupname) VALUES (?)"
val = ("测试","11111111","bb")
val1 = ['测试']
print(sql)
print(val)
cr.execute(sql)
#print(sql)
#cr.execute(sql.encode('GBK'))
conn.commit()

for row in results:
      comname = row[0]
      groupname = row[1]
      usercode = row[2]
      usernmae = row[3]
      post = row[4]
      postcode = row[5]
      # 打印结果
      print ("fname=%s|lname=%s|age=%s|sex=%s|income=%s|%s" % \
             (comname, groupname, usercode, usernmae, post,postcode ))

      #conn = pypyodbc.connect('DSN=yn5301;NEWCODESET=GB18030-2000,8859-1,819;CLIENT_LOCALE=en_US.utf8;DB_LOCALE=en_US.8859-1')
#--into temp t1 with no log; select * from t1

'''
conn=pypyodbc.connect('DSN=32_yn5301', unicode_results=False)

conn.cursor().execute('SELECT first * FROM lpzx_usercode').fetchone()[0].decode('UTF-8')

IBM INFORMIX ODBC DRIVER
print(results[0].decode('gbk'),\
	results[1].decode('GBK'),\
	results[2].decode('GBK'),\
	results[3].decode('GBK'),\
	results[4].decode('GBK'),\
	results[5].decode('GBK'))

	('测试','组','11111111','咔咔咔','','DDD')
'''