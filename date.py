import datetime as dt


class Date:

    def __init__(self):
        self.dt = dt.datetime
        self.now = dt.datetime.now()

    def today(self):
        t = self.dt.today()
        return str(t.strftime("%Y/%m/%d"))

    def yesterday(self):
        return str(self.dt.strftime(self.now - dt.timedelta(1), "%Y/%m/%d"))
