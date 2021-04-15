#!/usr/bin/python3
import os
import re
import datetime
import paramiko
import smtplib
# from email.mime.text import MIMEText
# from email.header import Header

process ="./test.lock"
os.system("ps -ef|grep test.py|grep -v grep >%s" % process)
if not(os.path.getsize(process)):
    print("morton - 1")
# os.system("nohup /home/languid/jiaoben.py %")
else:
    print("test - ok")