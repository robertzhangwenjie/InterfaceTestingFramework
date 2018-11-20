from builtins import object
from email.mime.application import MIMEApplication
from smtplib import SMTPException


import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data.get_email_data import GetEmailData



class SendEmail(object):

    def __init__(self,server_name='QQ'):
        email_data = GetEmailData()
        self.server_data = email_data.get_server_data(server_name)
        self.recivers = email_data.get_recivers_list()


    def send(self,subject,msg_text,filename=None):
        send_user = self.server_data['send_user']
        to_recivers = self.recivers['to_recivers']
        cc_recivers = self.recivers['cc_recivers']
        bcc_recivers = self.recivers['bcc_recivers']
        passwd = self.server_data['password']
        port = self.server_data['port']
        host = self.server_data['host']


        # message = MIMEText('test email','plain','utf-8')

        # message = MIMEText(msg,'html','utf-8')
        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = send_user
        message['To'] = ",".join(to_recivers)
        recivers = to_recivers
        if cc_recivers is not None:
            message['Cc'] = ",".join(cc_recivers)
            recivers.extend(cc_recivers)
        if bcc_recivers is not None:
            message['Bcc'] = ",".join(bcc_recivers)
            recivers.extend(bcc_recivers)
        if filename is not None and os.path.splitext(filename) == ".html":
            with open(filename,'rb') as fp:
                msg = fp.read()
                # 添加邮件附件 MIMEApplication可以表示Audio,html,Video等
                att1 = MIMEApplication(msg)
                att1.add_header('Content-Disposition', 'attachment', filename='result.html')
                message.attach(att1)
        #添加邮件正文
        message.attach(MIMEText(msg_text, 'plain', 'utf-8'))


        try:
            # 普通链接
            # with smtplib.SMTP(host="smtp.qq.com",port=25) as server:
            #     server.login(send_user,passwd)
            #     server.sendmail(send_user,recivers,message.as_string())

            #ssl俩姐
            with smtplib.SMTP_SSL(host,port) as server:
                server.login(send_user,passwd)
                server.sendmail(send_user,recivers,message.as_string())
            print('邮件发送成功')
        except SMTPException:
            print('Error: 发送邮件失败')

    def send_report(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # 成功率
        pass_result = "%.2f%%"%(pass_num/count_num*100)
        # 失败率
        fail_result = "%.2f%%"%(fail_num/count_num*100)

        sub = "接口自动化测试报告"
        msg_text = "此次一共运行接口个数为%d,成功率:%s,失败率:%s"%(count_num,pass_result,fail_result)
        self.send(sub,msg_text)



if __name__ == '__main__':
    pass_list = [1,2,34]
    fail_list = [1,2,34,4,5,6]

    se = SendEmail()
    se.send_report(pass_list,fail_list)


