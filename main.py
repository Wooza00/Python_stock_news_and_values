import smtplib
from news import News
from stock import Stock
from date import Date

EMAIL = "emailexample105@gmail.com"
PASS = "951753qwertY"


# ----- Stocks ----- # Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
date = Date()
stock = Stock()
news = News()

if stock.get_stock():
    print("GET NEWS")
else:
    print(f"NOTHING INTERESTING , ONLY CHANGE A {stock.get_stock()[1]}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

articles = news.get_news()
print(articles[0]['title'])
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_update(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=message
        )

#Optional: Format the SMS message like this:


c = 0
if stock.get_stock():
    for i in articles:
        to_send = f"TSLA: {stock.get_stock()[1]}\nHeadLine: {articles[c]['title']}\nBrief: {articles[c]['description']}"
        print(to_send)
        c += 1
    c = 0
else:
    print("NOTHING INTERESTING")


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

