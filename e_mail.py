#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from telnet_test import TelnetClient

class send_mail():
	my_sender='513656719@qq.com'    # 发件人邮箱账号
	my_pass = 'zlzyaaeplattbghh'              # 发件人邮箱密码
	my_user='513656719@qq.com'      # 收件人邮箱账号，我这边发送给自己
	def mail(msg,*b):
	    ret=True
	    try:
	        msg=MIMEText(msg,'plain','utf-8')
	        msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
	        msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
	        msg['Subject']="菜鸟教程发送邮件测试"                # 邮件的主题，也可以说是标题
	 
	        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
	        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
	        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
	        server.quit()  # 关闭连接
	    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
	        ret=False
	    return ret

	def mail_main():
		command = 'wc -l /app1/yn5301/sj/friday/bak/shenzhou/shenzhou_wj.csv'
		print(command)
		t =TelnetClient()
		c_result = t.cmd_run(command)
		print('============'+c_result)

		ret=send_mail.mail(c_result)
		if ret:
		    print("邮件发送成功")
		else:
		    print("邮件发送失败")

if __name__ == '__main__':
	#send_mail.mail_main()
	command = 'wc -l /app1/yn5301/sj/friday/bak/shenzhou/shenzhou_wj.csv'
	print(command)
	t =TelnetClient()
	c_result = t.cmd_run(command)
	print('============'+c_result)
	print('---------------')
	print(c_result[0])
	print('---------------')
	print(c_result[1])

	a = send_mail()
	ret=a.mail(c_result)
	if ret:
		print("邮件发送成功")
	else:
		print("邮件发送失败")