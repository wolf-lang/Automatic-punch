# -*- coding = utf-8 -*-
# @time 2020/12/28 18:43
# @Author 任乐乐
# @File POST
import json
import requests
import random

with open("001.txt", "r") as f:
    info = f.readlines()
    for i in range(len(info)):
        info[i] = info[i][:-1]

url = "http://yx.ty-ke.com/Home/Monitor/monitor_add"

heads = {
    "Cookie": "PHPSESSID=hgelg1i51rjc1rvshacbc5s3o0",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00; wv) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
    "Connection": "Keep-Alive",
    "Charset": "UTF-8",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "yx.ty-ke.com",
    "Content-Length": "330"
}

address = ["%e5%b1%b1%e8%a5%bf%e7%9c%81%e5%a4%aa%e5%8e%9f%e5%b8%82%e5%b0%96%e8%8d%89%e5%9d%aa%e5%8c%ba%e9%a6%a8%e5%9b"
           "%ad%e5%8d%97%e8%b7%af",
           "%e5%b1%b1%e8%a5%bf%e7%9c%81%e5%a4%aa%e5%8e%9f%e5%b8%82%e5%b0%96%e8%8d%89%e5%9d%aa%e5%8c%ba%e8%a1%8c%e7%9f"
           "%a5%e8%a5 "
           "%bf%e8%b7%af",
           "%e5%b1%b1%e8%a5%bf%e7%9c%81%e5%a4%aa%e5%8e%9f%e5%b8%82%e5%b0%96%e8%8d%89%e5%9d%aa%e5%8c%ba%e4%b8%9c%e7%8e"
           "%af",
           "%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%A4%AA%E5%8E%9F%E5%B8%82%E5%B0%96%E8%8D%89%E5%9D%AA%E5%8C%BAX256"]
for i in info:
    n = random.randint(0, 3)
    title = random.uniform(36.0, 36.8)
    data = "mobile={}&title={:.1f}&jk_type=%E5%81%A5%E5%BA%B7&wc_type=%E5%90%A6&jc_type=%E5%90%A6&province" \
           "=%E5%B1%B1%E8%A5%BF%E7%9C%81&city=%E5%A4%AA%E5%8E%9F%E5%B8%82&district=%E5%B0%96%E8%8D%89%E5%9D%AA%E5%8C%BA" \
           "&address={}" \
           "&is_verify=0 ".format(i, title, address[n])
    response = requests.post(url, headers=heads, data=data).text
    response = json.loads(response)
    if response['code'] == "400":
        print(i + response["msg"])
    else:
        continue


def send_email(str1):
    import smtplib
    from email.header import Header
    from email.mime.text import MIMEText

    smtpserver = "SMTP.qq.com"
    smtpport = 465
    from_mail = "3129289791@qq.com"
    to_mail = ["2103016836@qq.com"]
    password = "mlccvuyjdqjjfaga"  # 16位授权码

    str2 = ""
    for i in str1:
        str2 += i

    msg = MIMEText(str2, 'plain', 'utf-8')
    msg['From'] = Header("任乐乐", 'utf-8')  # 发送者
    msg['To'] = Header("测试", 'utf-8')  # 接收者

    subject = '打卡信息'
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, smtpport)
        smtp.login(from_mail, password)
        smtp.sendmail(from_mail, to_mail, msg.as_string())
    except smtplib.SMTPException as e:
        print(e.msg)
    finally:
        smtp.quit()

