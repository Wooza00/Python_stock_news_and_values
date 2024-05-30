import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_KEY = "ODRAU82CW5KR63GD"
ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
PARAM = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": ALPHA_VANTAGE_KEY,
}


class Stock:

    def __init__(self):
        self.r = None
        self.market_data = None

    def get_stock(self):
        self.r = requests.get(ALPHA_VANTAGE_ENDPOINT, PARAM)
        self.r.raise_for_status()
        data = self.r.json()
        self.market_data = data["Time Series (Daily)"]
        self.market_data = [i for i in self.market_data.items()]
        return self.compare(self.market_data)

    def compare(self, market_data):
        y_data = float(market_data[1][1]["4. close"])
        margin = (y_data*5)/100
        t_data = float(market_data[0][1]["4. close"])
        result1 = (y_data * 100)/t_data - 100
        if result1 > 0:
            result1 = f"🔺{result1}%"
        else:
            result1 = f"🔻{result1}%"
        if t_data < y_data - margin or t_data > y_data + margin:
            return True, result1
        else:
            return False, result1
