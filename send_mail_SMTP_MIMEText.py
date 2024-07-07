#内置库,用于连接服务器和登陆，发送邮件
import smtplib
#构造邮件
from email.mime.text import MIMEText

#smtp服务器地址
mail_host = "smtp.qq.com"
#用户名
mail_user = "XXXXXXX@qq.com"
#密码/授权码
mail_pwd = "cmyfXXXXXXXjja"
#指定发件人
me = "jomin<"+mail_user+">"
#收件人
mail_receiver = ["XXXXXXX@qq.com"]
#主题
mail_subject = "来自Jomin的问候"
#内容
mail_content = "You are so lucky!<br/>by Jomin"
#构造邮件内容(邮件内容、邮件类型、邮件编码)
#msg = MIMEText(mail_content,'plain','utf-8')#plain类型--纯文本，文本编码
msg = MIMEText(mail_content,'html','utf-8')
msg['Subject'] = mail_subject
msg['From'] = me
msg['To'] = ";".join(mail_receiver)

#发送邮件
#连接服务器
client = smtplib.SMTP_SSL(mail_host,465)
#登录服务器
client.login(mail_user,mail_pwd)
#发送
client.sendmail(me,mail_receiver,msg.as_string())
#退出
client.quit()