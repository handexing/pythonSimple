import smtplib
from email.mime.text import MIMEText

user = "908716835@qq.com"
pwd  = "xxxxxxxxxxx"
to   = "ant_li@qq.com"

def sendEmail(title,body):
    msg = MIMEText(body)
    msg["Subject"]=title
    msg["From"]=user
    msg["To"]= to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(user,pwd)
        s.sendmail(user,to, msg.as_string())
        s.quit()
        print("success!!!!")
    except smtplib.SMTPException:
        print("error!!!!")
    finally:
        s.close;

if __name__ == "__main__":
    sendEmail("hahahaha","hehehehehe...")
