##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

# 1. Update the birthdays.csv

birthdays = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv

today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if today in birthdays:

    # 3. If step 2 is true, pick a random letter from letter templates and replace
    # the [NAME] with the person's actual name from birthdays.csv

    person = birthdays[today]
    letter = random.randint(1, 3)

    with open(f"letter_templates/letter_{letter}.txt") as file:
        content = file.read()
        custom_content = str.replace(content, "[NAME]", person["name"])

        # 4. Send the letter generated in step 3 to that person's email address.

        my_email = "dummy.mail@gmail.com"
        password = "dummypassword"

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{custom_content}"
        )
        connection.close()
