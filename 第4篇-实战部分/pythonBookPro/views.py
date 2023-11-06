from concurrent.futures.thread import ThreadPoolExecutor
from email.mime.text import MIMEText
from django.http import HttpResponse
import smtplib
import logging


def sendEmailInhrit(request):
    sent = smtplib.SMTP()
    sent.connect('smtp.qq.com', 25)
    mail_name = "发送人邮箱地址"
    mail_password = "授权码"
    sent.login(mail_name, mail_password)
    to = ['收件人邮箱地址@qq.com']
    # 正文内容
    content = MIMEText('你好，我是Steafan')
    # 邮件标题
    content['Subject'] = 'Python高并发实践'
    content['From'] = mail_name

    sent.sendmail(mail_name, to, content.as_string())
    sent.close()
    return HttpResponse("success")


def logPrintDemo(self):
    logger = logging.getLogger('django')
    logger.info("This is anerror msg")
    return HttpResponse("打印日志成功，请在控制台查看")

# 高并发环境实现
# from email.mime.text import MIMEText
# from django.http import HttpResponse
# import smtplib
# from concurrent.futures import ThreadPoolExecutor
#
#
# def asyncSendEmail(request):
#     executor = ThreadPoolExecutor(max_workers=2)
#     executor.submit(sendEmailInhrit(request))
#
# def sendEmailInhrit(request):
#     sent = smtplib.SMTP()
#     sent.connect('smtp.qq.com', 25)
#     mail_name = "发送人邮箱地址"
#     mail_password = "授权码"
#     sent.login(mail_name, mail_password)
#     to = ['收件人邮箱地址@qq.com']
#     # 正文内容
#     content = MIMEText('你好，我是Steafan')
# # 邮件标题
#     content['Subject'] = 'Python高并发实践'
#     content['From'] = mail_name
#
#     sent.sendmail(mail_name, to, content.as_string())
#     sent.close()
#     return HttpResponse("success")


# def loggingPrintDemo():
#     logger = logging.getLogger('django')
#     executor = ThreadPoolExecutor(max_workers=2)
#     executor.submit(logger.info("This is anerror msg"))
