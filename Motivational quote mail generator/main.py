import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day = now.weekday()

with open("quotes.txt") as data:
    all_quotes = data.readlines()

if day == 1:
    random_quotes = random.choice(all_quotes)
    my_mail = YOUR_MAIL
    password = YOUR_MAIL_PASS_KEY
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail, to_addrs= TO_MAIL , msg=random_quotes)
    connection.close()