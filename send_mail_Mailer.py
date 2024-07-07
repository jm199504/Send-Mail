from mailer import Mailer
from mailer import Message
from email.header import Header

#smtp服务器地址
mail_host = "smtp.qq.com"
#用户名
mail_user = "XXXXX@qq.com"
#授权码
mail_pwd = "cmXXXXXXybjja"
#指定发件人
me = "xiaoming<"+mail_user+">"
#收件人（可设置多个接收邮箱号）
mail_receiver = ["XXXXXXXX@qq.com"]
#主题
mail_subject = Header("用python发送的邮件","utf-8").encode()
#内容
mail_content = "邮件内容balalala<br/>by Jomin"
#附件
mail_attach = "pic.jpg"
#设置邮件信息(发件人，收件人，字体编码，主题，内容，附件)
msg = Message(From=me,To=mail_receiver,charset="utf-8")
msg.Subject = mail_subject
msg.Html = mail_content
msg.attach(mail_attach)
#邮件参数（服务器地址，账号，密码，是否采用SSL模式）
client = Mailer(host=mail_host,pwd=mail_pwd,usr=mail_user,use_ssl=True)
#发送邮件
client.send(msg)

