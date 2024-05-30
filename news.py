import requests

NEWS_KEY = "49a0745939584d4da4a6688afdc042dd"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"
PARAM = {
    "apiKey": NEWS_KEY,
    "q": COMPANY_NAME,
}


class News:

    def __init__(self):
        self.r = None

    def get_news(self):
        self.r = requests.get(NEWS_ENDPOINT, PARAM)
        self.r.raise_for_status()
        data = self.r.json()
        news = data['articles']
        to_send = []
        for i in range(3):
            to_send.append(news[i])
        return to_send

