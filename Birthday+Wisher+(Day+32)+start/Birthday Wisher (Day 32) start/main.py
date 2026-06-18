import smtplib
import datetime as dt
import random

USER = "d81kumar13@gmail.com"
PASSWORD = "molatrrfhqzzehyg"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
      connection.starttls()
      connection.login(USER, PASSWORD)
      connection.sendmail(from_addr=USER,
                          to_addrs="an2016jan8@yahoo.com",
                          msg=f"subject:Morning Motivation\n\n{quote}")