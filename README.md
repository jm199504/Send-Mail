### 基于stmp/mailer批量发送邮件

![author](https://img.shields.io/static/v1?label=Author&message=junmingguo&color=green) 
![language](https://img.shields.io/static/v1?label=Language&message=python3&color=orange)
![topics](https://img.shields.io/static/v1?label=Topics&message=send-mail&color=blue)

### 1.基于stmp库批量发送邮件

STMP(Simple Mail Transfer Protocol)即简单邮件传输协议，它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

通过SMTP协议所指定的服务器，就可以把E-mail寄到收信人的服务器。

SMTP服务器则是遵循SMTP协议的发送邮件服务器，用来发送或中转发出的电子邮件。

SMTP 是一种TCP协议支持的提供可靠且有效电子邮件传输的应用层协议。SMTP 是建立在 TCP上的一种邮件服务，主要用于传输系统之间的邮件信息并提供来信有关的通知。

#### 1.1 运行流程

① 设置邮件参数(邮箱服务器地址、发件人邮箱号、密码、收件人邮箱号……)

② 设置邮件信息(主题、发件人名、内容、附件……)

③ 登录邮箱服务器

④ 登录邮箱账号

⑤ 发送邮件

⑥ 登出邮箱账号

#### 1.2 注意事项

- 邮箱设置开启SMTP/POP3的服务
- 开启POP3/SMTP服务，请务必备份好你的授权码
- SMTP_SSL端口号通常为465，并不是所有厂商的邮箱都是相同端口，每个邮箱服务器有对应不同的端口号，在邮箱的服务说明查看，例如：QQ邮箱设置账号>POP3/SMTP服务>(如何使用 Foxmail 等软件收发邮件？)

#### 1.3 发送邮件（仅文本）

```python
# pip3 install smtplib
# pip3 install email

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
```

#### 1.4 发送邮件（文本+附件：图片）

```python
# pip3 install smtplib
# pip3 install email

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
```



### 2.基于mailer库批量发送邮件

> 更少的代码实现email库中的MIMEMultipart的功能

#### 2.1 发送邮件（文本+附件：图片）

```python
# pip3 install mailer

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
```

