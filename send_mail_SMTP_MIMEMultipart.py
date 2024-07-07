#内置的库,用于连接服务器和登陆，发送邮件
import smtplib
#构造邮件
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText#文本类型
from email.mime.application import MIMEApplication#添加附件

#smtp服务器地址
mail_host = "smtp.qq.com"
#用户名
mail_user = "XXXXXXX@qq.com"
#密码/授权码
mail_pwd = "cmyXXXXXXXjja"
#指定发件人
me = "jomin<"+mail_user+">"
#收件人
mail_receiver = ["XXXXXXX@qq.com"]
#主题
mail_subject = "来自Jomin的问候"
#内容
mail_content = "You are so lucky!<br/>by Jomin"

#构造邮件体
msg = MIMEMultipart()#大盒子
msg['Subject'] = mail_subject
msg['From'] = me
msg['To'] = ";".join(mail_receiver)

#邮件主体
puretext = MIMEText(mail_content)
msg.attach(puretext)#构建一个纯文本puretext主题附加到msg
#附件xlsx
xlsxpart = MIMEApplication(open('pic.jpg','rb').read())
xlsxpart.add_header("Content-Disposition","attachment",filename="pic.jpg")#头文件，附件
msg.attach(xlsxpart)

#发送邮件
#连接服务器
client = smtplib.SMTP_SSL(mail_host,465)
#登录服务器
client.login(mail_user,mail_pwd)
#发送
client.sendmail(me,mail_receiver,msg.as_string())
#退出
client.quit()