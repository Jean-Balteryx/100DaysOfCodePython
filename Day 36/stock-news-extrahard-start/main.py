import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "7FNJH3IBZR2RTK2L"

NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = "2128f6ca7f294e06a2c82cd49aca1634"

TWILIO_ACCOUNT_SID = "ACeb1b8f647238fb1313e69c2ebdd37f50"
TWILIO_AUTH_TOKEN = "0d2d81fa63b8dbcc8a58b9c725e359aa"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
close_yesterday = data_list[0]["4. close"]
close_day_before_yesterday = data_list[1]["4. close"]

diff = round((float(close_yesterday) / float(close_day_before_yesterday) - 1) * 100, 1)

if abs(diff) >= 0:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()

    news = response.json()["articles"][:3]

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    percentage_message = ""

    if diff > 0:
        percentage_message += f"🔺{diff}%"
    else:
        percentage_message += f"🔻{diff}%"

    articles = [f"{STOCK}:{percentage_message}\nHeadline: {new['title']}\nBrief: {new['description']}" for new in news]

    for article in articles:
        message = client.messages \
                    .create(
                        body=article,
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

