import smtplib
import datetime as dt

# my_email = "jb.pinet@gmail.com"
# password = "servant-"
#
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="jbp.computing@gmail.com",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()


now = dt.datetime.now()
print(now)
print(type(now))

year = now.year
month = now.month
day_of_week = now.weekday()

print(year)
print(type(year))
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=11, day=24)
print(date_of_birth)