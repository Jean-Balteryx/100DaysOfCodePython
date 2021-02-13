import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API_KEY = "7FNJH3IBZR2RTK2L"
NEWS_API_KEY = "2128f6ca7f294e06a2c82cd49aca1634"
TWILIO_ACCOUNT_SID = "ACeb1b8f647238fb1313e69c2ebdd37f50"
TWILIO_AUTH_TOKEN = "38cb71543b3e3cc13097651d18fb82b5"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": AV_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

today = datetime.now().date()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))

close_yesterday = response.json()["Time Series (Daily)"][yesterday]["4. close"]
close_day_before_yesterday = response.json()["Time Series (Daily)"][day_before_yesterday]["4. close"]

diff = round((float(close_yesterday) / float(close_day_before_yesterday) - 1) * 100, 1)

if diff >= 5 or diff <= -5:
    print("Get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url="https://newsapi.org/v2/top-headlines", params=parameters)
    response.raise_for_status()

    data = response.json()["articles"]

    news = []
    if len(data) > 3:
        news_number = 3
    else:
        news_number = len(data)

    for i in range(news_number):
        news.append(data[i])

    print(news)

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    percentage_message = f"{STOCK}: "

    if diff > 0:
        percentage_message += f"🔺{diff}%"
    else:
        percentage_message += f"🔻{diff}%"

    message = client.messages \
                .create(
                    body=percentage_message,
                    from_="+15863718448",
                    to="+33665708618"
                )

    for new in news:
        new_message = f"Headline: {new['title']}\nBrief: {new['description']}"

        message = client.messages \
            .create(
            body=new_message,
            from_="+15863718448",
            to="+33665708618"
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

