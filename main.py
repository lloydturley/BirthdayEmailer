import datetime as dt
import random
import smtplib
import pandas


def send_email(subject, quote):
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user="dsfsdf@hotmail.com", password="")
        connection.sendmail(from_addr="dsfsdf@hotmail.com", to_addrs="adsfsd@gmail.com",
                            msg=f"Subject:{subject}\n\n{quote}")
    print("Email sent")


if dt.datetime.now().weekday() == 3:
    with open("quotes.txt") as file:
        lines = file.read().splitlines()

    line = random.choice(lines)
    # send_email("motivational quote", line)
else:
    print("uh oh")

data = pandas.read_csv("birthdays.csv")
all_dates = data.to_dict(orient="records")

# record = (n for n in all_dates if all_dates["month"]==4 and all_dates["day"]==25)

for each in all_dates:
    if each["month"] == dt.datetime.now().month and each["day"] == dt.datetime.now().day:
        letter_file_name = f"letter_{random.randint(1, 3)}.txt"
        with open(letter_file_name) as letter_file:
            generic_bday_letter = letter_file.read()

        custom_letter = generic_bday_letter.replace("[NAME]", each["name"])

        send_email("Happy Birthday!", custom_letter)
