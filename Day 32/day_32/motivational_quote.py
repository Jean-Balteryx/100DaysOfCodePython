import smtplib
import datetime as dt
import random

weekday = dt.datetime.now().weekday()

if weekday == 0:
    with open("quotes.txt") as file:
        quote = random.choice(file.readlines())

    my_email = "jb.pinet@gmail.com"
    password = "servant-"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="jbp.computing@gmail.com",
        msg=f"Subject:Monday's Quote\n\n{quote}"
    )
    connection.close()
