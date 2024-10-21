#导入smtplib模块
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from PIL import Image

neteaseMail = smtplib.SMTP_SSL('smtp.163.com', 465)
mailUser = "czkd35fromchina@163.com"
mailPass = "KRm9Dt6cmjK7eV3B"
neteaseMail.login(mailUser, mailPass)

#设置发件人和收件人
sender = "czkd35fromchina@163.com"
receiver = "yequbiancheng@baicizhan.com"
#使用MIMEMultipart,创建一个实例对象message
message = MIMEMultipart()

message["Subject"] = Header("给夜曲的一封信--Chen")
message["From"] = Header(f"czkd35<{sender}>")
message["To"] = Header(f"百词斩<{receiver}>")

textContent = ("你好，这是我用pytcharm发送的邮件。我的mac M1 芯片电脑上的VScode好像编译不了，我在网上查了好久也没解决这个问题。\n"
               "用自己写的python程序发送邮件感觉还挺有成就感的。\n"
               "基础课的学习内容感觉简单一些，平常没有怎么问过老师，最后发邮件实战，像我的VSCode用不了一些包就感觉卡壳很久。\n"
               "每天在这里练习感觉对编程还是有效果的，希望还能学习更多的知识。\n"
               "最后附上我的入门课成绩单和我IDE遇到的问题截图。")
mailContent = MIMEText(textContent, "plain", "utf-8")

filePath1 = ("/Users/mikechen/Desktop/score.jpg")
filePath2 = ("/Users/mikechen/Desktop/WechatIMG61.jpg")

"""
试验能否打开
img = Image.open(filePath)

img.show()
"""
with open(filePath1, 'rb') as imageFile:
    fileContent1 = imageFile.read()
with open(filePath2, 'rb') as imageFile:
    fileContent2 = imageFile.read()

#设置邮件附件，使用类MIMEImage，创建一个实例对象attachment

attachment1 = MIMEImage(fileContent1)
attachment2 = MIMEImage(fileContent2)

attachment1.add_header('Content-Disposition', 'attachment', filename="成绩单.jpg")
attachment2.add_header('Content-Disposition', 'attachment', filename="问题.jpg")

#添加正文：调用对象message的attach()方法
message.attach(mailContent)

message.attach(attachment1)
message.attach(attachment2)

neteaseMail.sendmail(sender, receiver, message.as_string())

print("发送成功")