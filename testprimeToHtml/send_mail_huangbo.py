# encoding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import sys

# 发送邮箱服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户/密码
user = 'chnhuangbo@163.com'
password = '********'
# 发送邮箱
sender = 'chnhuangbo@163.com'
# 接收邮箱
receiver = '18303974@qq.com'
# 发送邮件主题
subject = '生成Html报告-自动邮件发送源码-黄波'

# 发送的附件
sendfile = open(sys.path[0] + '/testprimeToHtml.zip', 'rb').read()

# 创建一个带附件的实例
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = Header(subject, 'utf-8')                         # 定义邮件标题
# 需要添加这两个赋值
msgRoot['From'] = sender
msgRoot['To'] = receiver

# 邮件正文内容
msgRoot.attach(MIMEText('刘老师，您好，我是黄波，这是根据今天上课内容修改的生成HTML报告和自动发送邮件源码。', 'plain', 'utf-8'))

# 构造附件
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="testprimeToHtml.zip"'
msgRoot.attach(att)

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()