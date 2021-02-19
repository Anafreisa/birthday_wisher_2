import datetime as dt
import pandas as pd
import random
import smtplib

my_email = YOUR EMAIL
password = YOUR PASSWORD

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

birthdays_df = pd.read_csv("birthdays.csv")
birthdays_dict = {
    (birthdays_df["month"], birthdays_df["day"]): birthdays_df
    for (index, birthdays_df) in birthdays_df.iterrows()
}
if today in birthdays_dict:
    birthdays_df_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_df_person["name"])

    with smtplib .SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{birthdays_df_person['email']}",
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )
