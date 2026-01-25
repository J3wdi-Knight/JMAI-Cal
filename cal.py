import calendar
from datetime import datetime


class Calendar:
    def __init__(self):
        self.date = datetime.now()

    def getCal(self):
        return calendar.month(self.date.year, self.date.month)
